#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Echo client program
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
# sever use setblocking or client use settimeout to prevent socket from blocking 
# s.setblocking(0) is equivalent to s.settimeout(0.0); s.setblocking(1) is equivalent to s.settimeout(None)
s.settimeout(5)

send_str='Hello, world;';
send_str = send_str * 500;

while send_str:
    bytes = s.send(send_str)
    send_str = send_str[bytes:]

data = []
while 1:
    try:
        recvData = s.recv(1024)
    except Exception,e:
        break
    else:
        if not recvData: break
        data.append(recvData)

s.close()
print 'Received:'
allLen = len(''.join(data))
print allLen