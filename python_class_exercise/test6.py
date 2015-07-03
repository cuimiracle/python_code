# -*- coding:utf-8 -*-
# import mock
# class ProcClass():
#     pass
   
# real = ProcClass()
 
#输入参数不影响行为的模拟
#模拟返回值
# real.method1 = mock.Mock(return_value = 3)
#模拟异常抛出
# real.method2 = mock.Mock(side_effect=KeyError('foo'))
 
# print real.method1()
# print real.method2()
# try:
#     real.method2()
# except KeyError,e:
#     print e


# 输入参数能影响行为的模拟
# aDict = {'a':1,'b':2,'c':3}
# def side_effect2(arg):
#     return aDict[arg]

# real.method3 = mock.Mock()
# real.method3.side_effect = side_effect2
# print real.method3('a')
# print real.method3('b')
# print real.method3('c')

# real.method4 = mock.Mock()
# real.method4.side_effect = [5,4,3,2,1]
# for i in real.method4.side_effect:
#     print i


####################################
# 不用MagicMock的时候
# amock =  mock.Mock()
# print str(amock)
# amock.__str__ =  mock.Mock(return_value = "where")
# print str(amock)
 
# 用MagicMock的时候
# from mock import MagicMock
# bMock = MagicMock()
# print str(bMock)
# bMock.__str__.return_value = "XXXXXX"
# print str(bMock)
####################################

# import subprocess
# ret = subprocess.check_output('ipconfig')
# 可以传第二个参数，比如'ls','-l'
# 管道，把上一个命令的标准输出作为下一个命令的标准输入
# ipconfig | find "net"
# print ret
# 把ifconfig的标准输出写入管道
# p1 =  subprocess.Popen(["ipconfig"],stdout = subprocess.PIPE)
# print p1.stdout.read()
# p2 = subprocess.Popen(["findstr","DNS"],stdin = p1.stdout,stdout=subprocess.PIPE)
# p2.communicate()

import threading,time,random,logging
# 在一个进程中启动多个线程(每个进程中至少包括一个主线程,文件描述符是全局变量
# 主线程和它的子线程是共享标准输出的，所以print可能没有来得及写换行符\n

def doWork(*args):
    print args
    #取当前线程的名字
    name = threading.current_thread().getName()
    print "%s start..." % name
    time.sleep(3)
    print "%s end..." % name

# doWork()
# 让doWork在aThread线程中运行
aThread =  threading.Thread(target = doWork,name="aThread")
# 创建一个子线程
# 用于io密集型，cpu密集型反而会时间更长，因为还包括了线程切换时间

bThread =  threading.Thread(target = doWork,name="bThread")

# 可以对调用的对象传递参数，参数是元组形式。
# 子线程传递参数，必须在创建线程之初传递过去
cThread =  threading.Thread(target = doWork,name="cThread",args=(1,2))

aThread.setDaemon(True)
bThread.setDaemon(True)
cThread.setDaemon(True)

# 开始跑子线程
aThread.start()
bThread.start()
cThread.start()

# join 阻塞当前线程，直到执行结束再执行其他线程
aThread.join()
bThread.join()
cThread.join()
# 等a线程,b线程和c线程都执行完毕，再计算cpu时间

doWork()

# 计算了所有cpu的执行时间（每个cpu都重头开始执行计算，然后叠加它们的时间）,
# 所以cpu密集型会超过真实运行时间，等待密集型会小于真实运行时间
print time.clock()
#############################################################################



#############################################################################

# lock = threading.Lock()
# a = 0
# def doWork2():
#     global a
#     for i in range(1000):
#         lock.acquire() #对非线程安全的对象一定要加锁，线程安全的对象则不用加锁
#         a +=1
#         lock.release()
#   
# aThread =  threading.Thread(target = doWork2,name="aThread")
# bThread =  threading.Thread(target = doWork2,name="bThread")     
#      
# aThread.start()
# bThread.start()
#   
# aThread.join()
# bThread.join()
# print a

# logging.basicConfig(
#     level = logging.DEBUG,
#     format='[%(levelname)s] (%(threadName)-10s)%(message)s'
# )
# def doWork3():
#    logging.debug("start...")
#    time.sleep(3)
#    logging.warn("start...")
#   
# aThread =  threading.Thread(target = doWork3,name="aThread")
# bThread =  threading.Thread(target = doWork3,name="bThread")     
#      
# aThread.start()
# bThread.start()
#   
# aThread.join()
# bThread.join()