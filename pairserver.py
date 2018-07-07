import zmq
import random
import sys
import time

import common




def setup(socket=None):
    if socket:
        socket.close()
    port = "5556"
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.RCVTIMEO = 5000
    socket.SNDTIMEO = 5000
    socket.bind("tcp://*:%s" % port)
    return socket


def run():
    socket = setup()
    while True:
        try:
            socket.send(common.MSG2)
            print('waiting for msg')
            msg = socket.recv()
            print(msg)
            time.sleep(0.125)
        except zmq.error.Again:
            print('Waiting for client')
            socket = setup(socket)


if __name__ == '__main__':
    run()
