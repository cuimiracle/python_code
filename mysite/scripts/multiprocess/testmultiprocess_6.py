#!/usr/bin/env python
# -*- coding:utf-8 -*-
import multiprocessing 

def f(ns,ls):
    ns.x = [1]
    temp_ls = ls[0]
    temp_ls[0] = 999
    ls[0] = temp_ls
    
if __name__ == '__main__':
    manager = multiprocessing.Manager()
    ns = manager.Namespace()
    ns.x = []
    ns.y = []
    ls = manager.list([[1],[2]])

    print 'before', ns, ls
    p = multiprocessing.Process(target=f, args=(ns,ls))
    p.start()
    p.join()
    print 'after', ns, ls