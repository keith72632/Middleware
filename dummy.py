import socket
from time import sleep
import sys

SERVER = '172.16.100.232' 
PORT = 6666
data = sys.argv[1]
with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
    s.connect((SERVER, PORT))
    print(f'Connected to server: {SERVER}')
    str_data = str(data)
    data = str_data.encode()

    try:
        s.send(data)
        print('Data sent')
    except KeyboardInterrupt:
        print('Keyboard Interrupt')
        s.close()
    except BrokenPipeError:
        print('Broken Pipe')

    s.close()
    print("Socket Closed\n")
