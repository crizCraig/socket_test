import zmq
import random
import sys
import time

import common

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)

total_size = 0

start = time.time()
last = start
last_window = start

while True:
    data = socket.recv()
    size = sys.getsizeof(data)
    # del data
    total_size += size
    socket.send(b"client message to server")
    now = time.time()

    if now - last > 1:
        print("bandwidth last 5 seconds is %dMB/s" % (total_size / (now - start) // 10**6))
        print("bandwidth last 5 seconds is %s/s" % common.sizeof_fmt(total_size / (now - start)))
        if now - last_window > 5:
            total_size = 0
            start = now
            last_window = now
        last = now


