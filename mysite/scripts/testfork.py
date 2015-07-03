#!/usr/bin/env python
#coding=utf8
 
import time,os
 
#创建子进程之前声明的变量
source = 10
 
try:
    pid = os.fork()
    print 'pid:'
    print pid
    if pid == 0: #子进程
        #在子进程中source自减1
        source = source - 1
        print "this is child process. Child Source:"
        print source
        time.sleep(30)
    else: #父进程
        source = source - 2
        print "this is parent process. Parent Source:"
        print source
    
except OSError, e:
    pass

#print:
#pid:
#10890
#this is parent process. Parent Source:
#8
#pid:
#0
#this is child process. Child Source:
#9