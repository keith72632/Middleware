import socket
import sys
import os
import subprocess
from threading import *
from datetime import datetime
from time import sleep


HOST = '172.16.100.232'
BB_PORT = 6666
WP_PORT = 8888
FILE_NAME = "logs.txt"

def log_handler(sock):
    f = open(FILE_NAME, "a")

    message = 'Address: ' + str(sock.getsockname()) + ' Time: ' + str(datetime.now()) + '\n\n' 

    f.write(message)

    file_size = os.path.getsize(FILE_NAME)

    f.close()

    if file_size >= 100000:
        os.system('rm logs.txt; touch logs.txt')
        print(f'{FILE_NAME} deleted')

def bb_thread():
    global DATA
    print(f'Thread {current_thread().getName()}')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
        s.bind((HOST, BB_PORT))

        s.listen(5)
        print(f'Listening...{s.getsockname()}')

        try:
            while True:
                conn, addr = s.accept()
                with conn:
                    data = conn.recv(1024)
                    data = data.decode()
                    if data:
                        print(f'Data: {data} from {conn.getsockname()} at {datetime.now()}')
                        DATA = data

        except KeyboardInterrupt:
            sys.exit(0)
            s.close()


def wp_thread():
    sleep(2)
    print(f'Thread {current_thread().getName()}')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
        s.bind((HOST, WP_PORT))

        s.listen(5)
        print(f'Listening...{s.getsockname()}')

        try:
            while True:
                conn, addr = s.accept()
                with conn:
                    data = str(DATA)
                    if data:
                        conn.send(data.encode())
                        print(f'Data: {data} sent to {conn.getsockname()} at {datetime.now()}')
                        log_handler(conn)
        except KeyboardInterrupt:
            sys.exit(0)
            s.close()

if __name__ == '__main__':

    t1 = Thread(target=bb_thread)
    t2 = Thread(target=wp_thread)
    t1.start()
    t2.start()


    t1.join()
    t2.join()

    print('works')
