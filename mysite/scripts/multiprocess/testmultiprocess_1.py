#!/usr/bin/env python
from multiprocessing import Process, Value, Array

def f(a):
    for i in range(len(a)):
        a[i] = -a[i]
    print 'sub process:'
    print a[:]

if __name__ == '__main__':
    arr = Array('i', range(10))
    #arr  = range(10)
    p = Process(target=f, args=(arr,))
    p.start()
    p.join()

    print 'main process:'
    print arr[:]