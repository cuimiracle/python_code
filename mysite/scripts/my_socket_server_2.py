#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Echo server program
import socket,threading

def handleRequest(conn, addr):   
    # sever use setblocking or client use settimeout to prevent socket from blocking 
    # s.setblocking(0) is equivalent to s.settimeout(0.0); s.setblocking(1) is equivalent to s.settimeout(None)
    # conn.setblocking(0)      

    while 1:
        try:
            recvData = conn.recv(1024)
        except socket.error:
            break
        else:
            if not recvData: break
            conn.sendall(recvData)
        
    conn.close()
    

        
def main():
    HOST = ''                 # Symbolic name meaning all available interfaces
    PORT = 50007              # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(2) # 如果单单使用主线程，不适用多线程的情况下，实际可以监听2+1=3个客户端
    
    while 1:  
        conn, addr = s.accept()
        print 'conn:'
        print conn
        print 'addr:'
        print addr
        handleRequest(conn, addr)
        
if __name__ == "__main__":  
    main()  