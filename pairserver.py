import zmq
import random
import sys
import time

import common

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)

while True:
    socket.send(common.MSG2)
    msg = socket.recv()
    time.sleep(0.125)
