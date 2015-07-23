from __future__ import print_function
from nanomsg import Socket, PAIR, PUB
import sys
import time

print "Listens on a socket for messages"
"""
Usage:
python python_test.py <socket_address>
Example: "python python_test.py tcp://127.0.0.1:49234"
Then you will need to create a source node with the same address tcp://127.0.0.1:49234 before calling this.
"""

receiver=Socket(PAIR)
receiver.connect(sys.argv[1])
while receiver.is_open():
	print "check:"+receiver.recv()
	time.sleep(1) #seconds

receiver.close()
