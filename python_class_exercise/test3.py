# -*- coding:utf-8 -*-

# for循环
# for i in range(0,30,3):
#     print i
# else:
#     print i

# for i in "hello":
#     print i

# for (x,y) in zip(list("hello"), list("world")):
#     print x,y

# for (x,y) in enumerate(list("hello")):
#     print x,y

# for x in list("hello"):
#     print x

# d = {'a':1, 'b':2}
# for x in d.keys():
#     print x,d[x]

# for x,y in d.items():
#     print x,y
# print d.items()

# test = [('a', 1), ('b', 2)]
# print test
# for (x,y) in test:
#      print x,y
# for x,y in test:
#      print x,y
# for x in test:
#     print x  
     
# for x in enumerate(list("hello")):
#     print x

# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         sys.stdout.write(str(j)+"*"+str(i)+"="+str(i*j)+" ")
#     sys.stdout.write("\n")

# 等腰三角形
# N = 3
# for i in range(N):
#     print " "*(N-1-i) + "*"*(2*i+1)

# 编写猜数字游戏
# from random import randint
# GUESS_MAX = 5
# c = randint(1,100)
# 
# count = 0
# while(count < GUESS_MAX):
#     a = raw_input("please input number:\n")
#     a = int(a)
#       
#     count = count + 1
#     if a > c:
#         print "too large"
#     elif a < c:
#         print "too small"
#     else:
#         print "good,right"
#         print ("count number times = %d" % count)
#         break
#   
# else:
#     print("answer = %d" % c)

# bStr = "abcdefgad"
# aDict = {}
# for i,j in enumerate(bStr):
#     aDict.setdefault(j, [])
# #    aDict[j] = aDict.get(j,[])
#     aDict[j].append(i)
# 
# for i in sorted(aDict):
#     print i, "=>", aDict[i]


import sys
# alist = sys.argv
# aList = [float(item) for item in sys.argv[1::]]
# print sorted(aList,None,None,False)
# print aList
# print "%.2f" % sum(aList)

# print "%(key1)d %(key2)s" % {"key2":"abc","key1":123}

# from pprint import pprint
# aDict = {i:range(i) for i in range(1,7)}
# pprint(aDict)

# from optparse import OptionParser
 
# for line in open("a.txt"):
#     print line

# 文件重定向
# aFile = open("a.txt","w")
# tmp = sys.stdout
# sys.stdout = aFile
#  
# print "Hello 2"
# print "Hello 3"
# aFile.flush()
# aFile.close()
# sys.stdout = tmp
# print 'yes'



# 序列化对象
# F = open('test.txt', 'w')
# import pickle
# pickle.dump({"a":1, "b":2},F)
# F.close()
# F = open('test.txt')
# E = pickle.load(F)
# print E

#方法1
# aFile = open("b.txt","r")
# sum = 0
# for line in aFile:
#     sum += int(line.split()[-1]);
# print sum
#方法2
#print sum([int(line.split()[-1]) for line in open("a.txt","r")])


# for line in open("b.txt","r"):
#     sys.stdout.write(line) 
#     print line


#######################################################

# 函数
# def aFun():
#     '''This is subject
#     
#     This is content1
#     This is content2
# '''
#     return 2
# 
# print aFun.__doc__
# help(aFun) #和aFun.__doc__一样可以查看注释

# 局部变量
# aStr = "64"
# def aFun():
#     aStr = "32"
#     
#     def bFun():
#         print aStr
#         
#     return bFun
# 
# cFun = aFun()
# cFun()
# print aStr 

# aStr = "64"
# def aFun():
#     bStr = "64"
#     print id(bStr)
#     return bStr
#  
# print id(aStr)
# aFun()

# 非键值对变参(打印出元组)
# def sumFun(*i):
#     print i
# sumFun(4,5,6,"Hello")

# 键值对变参(打印出字典)
# def sumFun(**i):
#     print i
# sumFun(a=4,b=5,c=6,d="Hello")


# print (lambda x,y : x**y)(2,4)

