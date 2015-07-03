#!/usr/bin/env python
# -*- coding:utf-8 -*-

# To create one’s own manager, one creates a subclass of BaseManager and uses the register() classmethod to register new types or callables with the manager class.
from multiprocessing.managers import BaseManager

class MathsClass(object):
    def add(self, x, y):
        return x + y
    def mul(self, x, y):
        return x * y

class MyManager(BaseManager):
    pass

MyManager.register('Maths', MathsClass)

if __name__ == '__main__':
    manager = MyManager()
    manager.start()
    maths = manager.Maths()
    print maths.add(4, 3)         # prints 7
    print maths.mul(7, 8)         # prints 56