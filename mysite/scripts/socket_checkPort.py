#!/usr/bin/env python
import socket
import sys

def checkPort(address, port):
    #create a TCP socket
    s =  socket.socket()
    print "-> %s:%s" % (address, port)
    try:
        s.connect((address, port))
        print "connect OK"
        return True
    except socket.error,e:
        print "connect failed:%s" % e
        return False
    
if __name__ == "__main__":
   r = checkPort("g.cn",80)
   print 'checkPort:%s' % r
   sys.exit(not r)