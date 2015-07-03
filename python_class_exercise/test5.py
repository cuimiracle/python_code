# -*- coding:utf-8 -*-
# 自定义异常
# class UserError(Exception):
#     def __init__(self, expression, msg):
#         self.expression = expression
#         self.message = msg
# try:
#     raise UserError('test','test2')
# except UserError,e:
#     print e.expression
#     print e.message

# 队列
# class Queue(list):
#     def push(self, item):
#         self.append(item)
#     def pull(self):
#         try:
#             ret =  self[0]
#         except IndexError,e:
#             raise IndexError("Queue is empty")
#         
#         del self[0]
#         return ret
#         
# aStack = Queue()
# aStack.push("hello")
# aStack.push("42")
# print aStack.pull()
# print aStack.pull()
# print aStack.pull()

import re
# reCmp = re.compile("ht+p",re.I | re.MULTILINE)
# if reCmp.search("Hp404\nHtttttP4"):
#     print "Match!"
# else:
#     print "non-Match"
    
    
# line = "Code:A127Z"
# match = re.search('(\w)((\d{3})(\w))',line)
# items = match.groups()
# print items
# reCmp = re.compile('(\w)((\d{3})(\w))')
# items = reCmp.findall(line)
# print items

# line="This is fun"
# print re.sub("i\w","was",line)
# line = "dog,dog,dog"
# print re.sub("d.g","cat",line,2)

# reCmp = re.compile(r"(.{3,}).*\1")
# if reCmp.search("123456890456"):
#     print 'match'


# reCmp = re.compile("(\d*)[2-9]\d{4}\d*")
# aList = [line for line in open("a.txt") if reCmp.search(line)]
# print aList
# bList = [reCmp.findall(line) for line in aList]
# print bList
# bList = [['20001'],['20001','2222222']] 
# print reduce(lambda x,y:x+y,bList)

# N = 5
# aList = []
# try:
#     with open("a.txt") as aFile:
#         for line in aFile:
#             line = line.rstrip("\n")
#             aList.append(line)
#             aList.sort(reverse =  True)
#             if len(aList) > N:
#                 del aList[N:]
# except IOError:
#     print "couldn't open!"
# print ",".join(aList)

# 生成器函数，返回值是一个生成器对象
# def genSeq(N):
#     for i in range(N):
#         yield i**2
#  
# a = genSeq(10)
# print a
# for i in a:
#     print i
# 生成器for循环用完之后就没有了，只能迭代一次的叫做单迭代对象。
# 然后用完的生成器由于没有变量指向它，最后会被垃圾回收机制回收。

# a=(i for i in range(5))
# print a
# for i in a:
#     print i
# 生成器表达式也能返回一个生成器
# iter生成器,生成一个单迭代对象

# 生成器和迭代器部分的习题
# 打印N以内的斐波那契数列(N=1000)    
# a,b = 1,2
# while True:
#     print b
#     a,b = b,a+b
#     if b>1000:
#         break;
#  
# def genSeq():
#     a,b = 1,2
# #    yield a
# #    yield b
#     while True:
#         a,b = b,a+b
#         yield b 
# #        相当于push to list
#   
# shengchengqi = genSeq()
#   
# for i in shengchengqi:
#     if i < 1000:
#         print i
#     else:
#         break;
     
  
    