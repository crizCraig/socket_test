import sys
import socket
import numpy as np

MSG = b'x' * int(1 * 10 ** 3.5)
MSG2 = b'10001'*(10**8*2)
NUMPY_ARRAY = np.random.rand(3,2)
MSG_LENGTH = sys.getsizeof(MSG)
MSG2_LENGTH = sys.getsizeof(MSG2)
SEND_BUF_SIZE = int(2.5E6)
RECV_BUF_SIZE = int(2.5E6)

HOST = 'localhost'
PORT = 50007


def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

print('message length', sizeof_fmt(MSG_LENGTH))
print('message2 length', sizeof_fmt(MSG2_LENGTH))


def configure_socket(s):
    buffer_size = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Buffer size [Before]:%d" % buffer_size)
    s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    s.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        SEND_BUF_SIZE)
    s.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,
        RECV_BUF_SIZE)
    buffer_size = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Buffer size [After]:%d" % buffer_size)


