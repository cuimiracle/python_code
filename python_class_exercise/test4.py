# -*- coding:utf-8 -*-
# line = [line for line in open("a.txt","r")]
# for line in open("a.txt"):
#     print line
# Run:python printLong.py a.txt
# print "-----------------"
# import sys
# fileName = sys.argv[1]
# fileName = "a.txt"
# print reduce(lambda x,y:x if len(x)>len(y) else y,open(fileName))
# aList = ['Hello 1','Hello 22','Hello 333','Hello 4444']
# print reduce(lambda x,y:x if len(x)>len(y) else y, aList)

    
# aTuple = (5,3)
# print divmod(*aTuple)

# print pow(3,4)
# print map(pow,[1,2,3],[2,3,4])
# print map(pow,*([1,2,3],[2,3,4]))
# print range(1,5)
# print reduce((lambda x,y:x+y),range(1,5))

# def sumAny(*args):
#     return reduce((lambda x,y:x+y),args)
# print sumAny("hello"," ","world")

# def Fun(num):
#     return reduce((lambda x,y:x+y),range(num))
# print Fun(5)

# 递归

# def aFun(aInt):
#     return aInt if aInt < 3 else aFun(aInt-1) + aFun(aInt-2)
# print aFun(40)

# 递推
# def bFun(aInt):
#     aList = []
#     for i in range(1,aInt+1):
#         aList.append(i if i<3 else sum(aList[-2:]))
#     return aList[-1]
# print bFun(40)

# 打印输出符合如下条件之一的100以内的自然数
# （1）能被30整除
# （2）个位+十位=10
# （3）个位-十位=5
# funList = [lambda x: x%3==0,
#            lambda x: x%10+x/10==10,
#            lambda x: x%10-x/10==5]
#  
# def testFun(i):
#     return any(fun(i) for fun in funList)
#  
# print filter(testFun, range(20))

# 实现一个函数，将字符串序列按长度排序
# ['bool','hello','smiles','objective']
 
# def sortStrbyLen(x,y):
#     return cmp(len(x),len(y))
#   
# testStrList = ['hello','smiles','bool','objective']
# print sorted(testStrList,cmp=sortStrbyLen)


# 按字典的值排序
# def sortStrbyLen(x,y):
#     return cmp(aDict[x],aDict[y])
# aDict = {'a':1,'b':3,'c':2,'d':4}
# sorted(aDict,cmp=sortStrbyLen)
# print aDict
 
# for i in sorted(aDict,cmp=sortStrbyLen):
#     print i,aDict[i]

# 方法工具
# import functools
# aFun = lambda x: pow(x,6)
# 动态生成函数对象,第二个参数可以指定第一个函数中的默认值
# int2 = functools.partial(int, base=2)
# print int2("100000")
# print int2("100000",base=10)

# for (x,y) in enumerate(list("hello")):
#     print x,y

# import sys,pprint
# pprint.pprint(sys.path)
# sys.path.append("testPkg")
# 
# import testModule2


# import math
# funList = [attr for attr,value in math.__dict__.items() if callable(value)]
# fieldList = [attr for attr,value in math.__dict__.items() if not callable(value)]
#  
# print funList
# print fieldList
# print "-------------------------------------------------------"
# print math.fsum.__doc__

# class A():
#     aField =3
#     def aMethod(self):
#         print "aMethod"
#   
# a = A()
# print a.aField
# print a.aMethod()
# print "-------------------------------------------------------"
# print A.aField
# print A.aMethod(a)
