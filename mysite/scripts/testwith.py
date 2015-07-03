#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
class test:
    def __enter__(self):
           print("enter")
           return 1
    def __exit__(self, *args):
           print("exit")
           #  return False
           return True
with test() as t:
    print("t is not the result of test(), it is __enter__ returned")
    print("t is 1, yes, it is {0}".format(t))
    raise NameError("Hi there")
    sys.exit()
    print("Never here")
    
# 1，t不是test()的值，test()返回的是"context manager object"，是给with用的。t获得的是__enter__函数的返回值，这是with拿到test()的对象执行之后的结果。t的值是1.
# 2，__exit__函数的返回值用来指示with-block部分发生的异常是否要re-raise，如果返回False，则会re-raise with-block的异常，如果返回True，则就像什么都没发生。
