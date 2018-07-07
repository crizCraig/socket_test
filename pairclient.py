import zmq
import random
import sys
import time
import pyarrow
import numpy as np

import common


def setup(socket=None):
    if socket:
        socket.close()
    port = "5556"
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.RCVTIMEO = 5000
    socket.SNDTIMEO = 5000
    socket.connect("tcp://localhost:%s" % port)
    return socket


def run():
    total_size = 0

    start = time.time()
    last = start
    last_window = start

    index = 0

    socket = setup()

    while True:
        try:
            data = socket.recv()
            size = sys.getsizeof(data)
            nparray = np.frombuffer(data)
            print('nparray shape', nparray.shape)
            # del data
            total_size += size
            socket.send(b"client message to server %d" % index)
        except zmq.error.Again:
            print('Waiting for server')
            socket = setup(socket)

        index += 1
        now = time.time()

        if now - last > 1:
            print("bandwidth last 5 seconds is %dMB/s" % (total_size / (now - start) // 10**6))
            print("bandwidth last 5 seconds is %s/s" % common.sizeof_fmt(total_size / (now - start)))
            if now - last_window > 5:
                total_size = 0
                start = now
                last_window = now
            last = now


if __name__ == '__main__':
    run()

