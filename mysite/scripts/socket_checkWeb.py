#!/usr/bin/env python
import httplib
import socket
import sys
from pip._vendor.distlib._backport.tarfile import TUREAD

def checkWeb(a, p, resource):
    if not resource.startswith('/'):
        resource = '/' + resource
    try:
        con = httplib.HTTPConnection(a,p)
        con.request('GET', resource)
        response = con.getresponse()
    except socket.error,e:
        return False
    finally:
        con.close()
    if response.status in [200, 300]:
        return True
    return False
    
if __name__ == "__main__":
   r = checkWeb("www.baidu.com", 80, "/")
   print 'resource:%s' % r
   sys.exit(not r)