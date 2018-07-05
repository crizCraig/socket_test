from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from future.builtins import (ascii, bytes, chr, dict, filter, hex, input,
                             int, map, next, oct, open, pow, range, round,
                             str, super, zip)
from collections import OrderedDict
import json
import zmq


# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.SUB)

# Define subscription and messages with prefix to accept.
prefix = 'deepdrive-dashboard'
sock.setsockopt_string(zmq.SUBSCRIBE, prefix)
sock.connect("tcp://127.0.0.1:5680")

while True:
    message = sock.recv()
    message = message[len(prefix)+1:]
    olist = json.loads(message.decode('utf8').replace("'", '"'))
    print(olist)
