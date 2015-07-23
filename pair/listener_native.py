#!/usr/bin/python
import socket               # Import socket module
import sys

"""
usage:
python listener_native.py ipc:///tmp/pipeline.ipc
for shared memory usage or
python listener_native.py tcp://127.0.0.1:49234
for distribtued machines.
NOTE: THIS IMPLEMENTATION DOES NOT WORK YET!
"""

def myreceive(sock):
    chunks = []
    bytes_recd = 0
    while bytes_recd < MSGLEN:
        chunk = sock.recv(min(MSGLEN - bytes_recd, 2048))
        #if the other side closes the connection
        #For python, you'll read a zero length string, or a socket.error will be thrown when you try to read or write from the socket.
        if chunk == '':
            raise RuntimeError("socket connection closed/broken")
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)
    return ''.join(chunks)

if (len(sys.argv)<2):
    raise Exception("ERROR: You need to pass the address of the socket")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url= ":".join(sys.argv[1].split(":")[:-1])
port=int(sys.argv[1].split(":")[-1])
print "Url: "+str(url)+", port: "+str(port)

#bind or connect?
#s.bind((url, port))

s.connect((url, port))

while (True):
    res=myreceive(s)
    print "Areceivedwer: "+str(res)

s.close()
