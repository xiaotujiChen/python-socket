# Send UDP broadcast packets

MYPORT = 50000

import sys, time
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
#s.connect(('', 50000))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while 1:
    data = 'hello'
    s.sendto(data, ('<broadcast>', MYPORT))
    time.sleep(2)