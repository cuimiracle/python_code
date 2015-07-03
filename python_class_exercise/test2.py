# -*- coding:utf-8 -*-
import math
import random
# aList = [1,3,1,2,7,4,6]
# print id(aList)

# aList.append(4)
# aList.append([4, 5])
# aList.extend([4, 5])
# aList.sort() 

# aList.insert(1, 4) # 在1后面插入4，只插入一次
# aList.reverse()

# aList.pop(4) 

# aList.remove(1) # 删除1，只删除一次

# del aList[2] # 删除列表中索引为2的元素

# del aList[0: 1]

# print id(aList)

# aList[2] = 5

# aList[1:3] = [4, 5, 6] 

# print aList;
# exit()

# L2 = [x for x in range(5)]
# print L2;

# L2 = [x ** 2 for x in range(5)]
# print L2;

# L2 = [x ** 2 for x in range(5) if x > 3]
# print L2;
# exit()

# L2 = zip([1, 2, 3], ["apple","pear","banana"])
# print L2;

# str1 = "hello"
# print tuple(str1);

# x = "haha"
# y = 5
# x,y = y,x
# print x
# print y

# print [x**2 for x in range(100) if x**2 <= 100]
# print [x**2 for x in range(int(math.ceil(101**(1.0/2))))]

# print math.sqrt(2)

# list = sorted("hello")[::-1]
# print list
##############################################################
# input = "aaa bbb ccc";
# input = input.split();
# print input

# list = sorted("hello", reverse = True)
# print list
# print ",".join(list)

# input = raw_input("please input")
# input = list(input)
# print "".join([str(ord(x)) for x in input])
 
# input = raw_input("please input")
# input = input.split();
# print [int(x)**2 for x in input]
  
# input = raw_input("please input")
# input = input.split();
# input = [int(x) for x in input]
# print " ".join(str(x) for x in sorted(input,reverse=True))
 
# first = raw_input("first")
# second = raw_input("second")
# third = raw_input("third")
#  aList = list();
#  print aList

# aList.append(first) 
# aList.append(second) 
# aList.append(third) 


# input = raw_input("please input")
# list = ['shu','niu','hu','tu','long','she','ma','yang','hou','ji','gou','zhu']
# index = (int(input)-1984)%12
# index = (int(input)-1989+5)%12
# print list[index]

# aList = [1,2,3,4,5,6,7]
# aList.remove(max(aList))
# aList.remove(min(aList))
# print aList
# aList = [int(x) if x.isdigit else 0 for x in aList]
# print float(sum(aList))/len(aList)
# aList = aList[1:-1]
# print aList
# print float(sum(aList))/len(aList)

# aList = [1,2,3,4,5,6,7]
# temp = list();
# temp2 = list();
# for x in range(10000):
#     temp.append(random.choice(aList));
# temp = [random.choice(aList) for x in range(10000)]
# temp2 = [str(x)+":"+str(temp.count(x)) for x in aList]
# for x in aList:
#     print temp.count(x)
# print temp
# c = [(i, temp.count(i)) for i in aList]
# print c
# for x,y in c:
#     print("%d => %d" % (x,y))

# print range(0,50,3)
# print range(50)[::3]

# a = set("hello")
# b=set(['y','e']);
# x = 'p'
# a.update(b)    # a集合和b集合的并集
# a.intersection_update(b)    # a集合和b集合的交集
# a.difference_update(b)  # a集合-b集合
# a.symmetric_difference_update(b)    # a集合和b集合的差集
# a.add(x)
# a.remove(x)    # if x is not exist,it will throw error exception
# a.discard(x)    # remove if exist
# a.pop()
# a.clear()
# print a
# exit()

# d = {'apple': 1.5, 'pear': 2.3}
# e = dict(apple = 1.5, pear = 2.3)
# f = dict([("apple",1.5),("pear",2.3)])
# print d
# print e
# print f

# print d.get('apple')
# print d.get('apple1','default')
# print d.pop('apple','default')
# print d

# print d.items()
# print d.keys()
# print d.values()
# exit()

# for x,y in d.items():
#     print("%s => %s" % (x,y))
# exit()


# cset = set("translation")
# print len(cset)
# exit()

# set1 = set("smiles")
# set2 = set("smart")
# print set1 & set2   # 交集
# print set1 ^ set2   # 差集
# set1.symmetric_difference_update(set2)
# print(set1)
# exit()

# clist = list("translation")
# cset = set("translation")
# print {x:clist.count(x) for x in cset}


# from collections import Counter
# aList = list("translation")
# aListCounter = Counter(aList)
# print aListCounter
# exit()
 
# aStr = 'it is my book.'
# wordList = [word for word in aStr.split() if word.isalpha()]
# print wordList
# exit()

# # 根据首字母对列表内元素进行归类
# wordList = ['it', 'is', 'my', 'book']
# aDict = {}
# for word in wordList:
#     firstChar = word[0]
#     aDict[firstChar] = aDict.get(firstChar,[])
# #   aDict[firstChar] = aDict.setdefault(firstChar,[])
# #   aDict[firstChar] = aDict.get(firstChar)
#     aDict[firstChar].append(word)
#     
# print aDict.items()
# 
# for tempKey,tempValue in aDict.items():
#     print("%s => %s" % (tempKey,tempValue))

# d = {"apple":15,"pear":20,"banana":10}
# sortKeys = sorted(d.keys())
# 
# for x in sortKeys:
#     print x,d[x]


# d = {"apple":15,"pear":20,"banana":10}
# k = d.keys()
# v = d.values()
# 
# print {x for x in range(len(d))}
# print {v[x]:k[x] for x in range(len(d))}
# print zip(d.values(),d.keys())
# print dict(zip(d.values(),d.keys()))


#根据用户的需求(raw_input)查询d字典中的水果价格,如果用户查询的水果不存在,返回"None"
# d = {"apple":15,"pear":20,"banana":10}
# input = raw_input("input please")
# print d.get(input,"None")

