from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from future.builtins import (ascii, bytes, chr, dict, filter, hex, input,
                             int, map, next, oct, open, pow, range, round,
                             str, super, zip)
import zmq
import time
import json
from collections import deque, OrderedDict


# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.PUB)
sock.bind("tcp://127.0.0.1:5680")

zmq_id = 0

display_stats = OrderedDict()
display_stats['g-forces']                      = {'total': 0, 'value': 0, 'ymin': 0,     'ymax': 3,    'units': 'g'}
display_stats['gforce penalty']                = {'total': 0, 'value': 0, 'ymin': -500,  'ymax': 0,    'units': ''}
display_stats['lane deviation penalty']        = {'total': 0, 'value': 0, 'ymin': -500,  'ymax': 0,    'units': ''}
display_stats['lap progress']                  = {'total': 0, 'value': 0, 'ymin': 0,     'ymax': 100,  'units': '%'}
display_stats['episode #']                     = {'total': 0, 'value': 0, 'ymin': 0,     'ymax': 5,    'units': ''}
display_stats['time']                          = {'total': 0, 'value': 0, 'ymin': 0,     'ymax': 250,  'units': 's'}
display_stats['episode score']                 = {'total': 0, 'value': 0, 'ymin': -500,  'ymax': 2000, 'units': ''}

while True:
    time.sleep(1)
    zmq_id, now = zmq_id + 1, time.ctime()

    # Message [prefix][message]
    message = "deepdrive-dashboard-{msg}".format(msg=json.dumps(list(display_stats.items())))
    start = time.time()
    sock.send_string(message)
    end = time.time()
    print('took %fs' % (end - start))

    zmq_id += 1
