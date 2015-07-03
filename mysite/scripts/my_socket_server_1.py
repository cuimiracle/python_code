#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Echo server program
import socket,threading

def handleRequest(conn, addr):   
    # sever use setblocking or client use settimeout to prevent socket from blocking 
    # s.setblocking(0) is equivalent to s.settimeout(0.0); s.setblocking(1) is equivalent to s.settimeout(None)
    conn.setblocking(0)      

    while 1:
        try:
            recvData = conn.recv(1024)
        except socket.error:
            break
        else:
            if not recvData: break
            conn.sendall(recvData*10)
        
    conn.close()
    

        
def main():
    HOST = ''                 # Symbolic name meaning all available interfaces
    PORT = 50007              # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    
    while 1:  
        conn, addr = s.accept()
        print 'conn:'
        print conn
        print 'addr:'
        print addr
        newThread = threading.Thread(target=handleRequest, args=(conn, addr))
        newThread.setDaemon(True)
        newThread.start()
        
if __name__ == "__main__":  
    main()  