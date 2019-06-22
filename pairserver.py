import pyarrow
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

    # socket.RCVTIMEO = 5000
    # socket.SNDTIMEO = 5000
    socket.bind("tcp://*:%s" % port)

    poller = zmq.Poller()
    poller.register(socket, zmq.POLLIN | zmq.POLLOUT)
    while dict(poller.poll())[socket] != zmq.POLLOUT:
        time.sleep(0.001)

    return socket, poller


def run():
    socket, poller = setup()
    while True:
        try:
            socket.send(pyarrow.serialize(common.NUMPY_ARRAY).to_buffer())
            print('waiting for msg')
            msg = wait_for_msg(socket, poller)
            print(msg)
            time.sleep(0.125)
        except zmq.error.Again:
            print('Waiting for client')
            socket = setup(socket)


def wait_for_msg(socket, poller):
    while True:
        socks = dict(poller.poll())
        if socket in socks and socks[socket] == zmq.POLLOUT|zmq.POLLIN:
            msg = socket.recv()
            return msg
        else:
            time.sleep(1e-6)


if __name__ == '__main__':
    run()
