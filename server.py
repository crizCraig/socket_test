# Echo server program
import socket
from common import *

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    configure_socket(s)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, address = s.accept()
    with conn:
        print('Connected by', address)
        while True:
            data = conn.recv(MSG_LENGTH)
            if not data:
                break
            conn.sendall(data)
