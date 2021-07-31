from threading import *
from thread_tasks import *

def main():
    t1 = Thread(target=bb_thread)
    t2 = Thread(target=wp_thread)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    main()

