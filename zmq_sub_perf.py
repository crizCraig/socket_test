import sys
import time
import common

import zmq

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 = sys.argv[2]
    int(port1)

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from weather server...")
socket.connect("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
    socket.connect("tcp://localhost:%s" % port1)

# Subscribe to zipcode, default is NYC, 10001
topicfilter = b"0"
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

total_size = 0
start = time.time()
end = start
for update_nbr in range(100):
    string = socket.recv()
    topic, index, data = string.split()
    size = sys.getsizeof(data)
    total_size += size
    print('received data size of %r index %r' % (size, index))
    now = time.time()

    if now - end > 1:
        print("bandwidth is %dMB/s" % (total_size / (now - start) // 10**6))
        print("bandwidth is %s/s" % common.sizeof_fmt(total_size / (now - start)))
        end = now
