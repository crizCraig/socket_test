import zmq
import random
import sys
import time
import common

port = "5556"

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

data = common.MSG2
index = 0

while True:
    topic = 0
    # messagedata = random.randrange(1, 215) - 80
    # print("%d %d" % (topic, data))
    socket.send(b"%d %d %b" % (topic, index, data))
    print('sent data %r' % index)
    time.sleep(0.125)
    index += 1
