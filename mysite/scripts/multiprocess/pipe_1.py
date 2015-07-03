#!/usr/bin/env python
from multiprocessing import Pipe
a, b = Pipe()
# a.send([1, 'hello', None])
# b_recv = b.recv()
# print 'b_recv:'
# print b_recv
# 
# b.send_bytes('thank you')
# a_recv = a.recv_bytes()
# print 'a_recv:'
# print a_recv

import array
arr1 = array.array('i', range(5))
arr2 = array.array('i', [0] * 10)
# print 'arr1:'
# print arr1.itemsize
# print len(arr1)
# print 'arr2:'
# print arr2.itemsize
# print len(arr2)

a.send_bytes(arr1)

count = b.recv_bytes_into(arr2)
print 'count:'
print count
assert count == len(arr1) * arr1.itemsize
print arr2