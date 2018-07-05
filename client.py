# Echo client program
import socket
from common import *
import time


def main():
    i = 0
    total_time = 1E-9  # Avoid divide by zero
    total_size = 0
    last_print_time = 0

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        configure_socket(s)
        s.connect((HOST, PORT))
        while True:
            start = time.time()
            s.sendall(MSG)
            data = s.recv(MSG_LENGTH)
            end = time.time()
            total_time += end - start
            size = sys.getsizeof(data)
            # if size != MSG_LENGTH:
            #     print('size', size, 'does not equal message length', MSG_LENGTH)
            total_size += size

            if end - last_print_time > 1 and total_time > 0:
                last_print_time = end
                bandwidth = 2 * total_size / total_time  # bi-directional so 2 times

                print(sizeof_fmt(bandwidth), '/s')
            i += 1
            # print('Received', repr(MSG))




if __name__ == '__main__':
    sys.exit(main())
