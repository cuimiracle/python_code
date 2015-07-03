#!/usr/bin/env python
# -*- coding:utf-8 -*- 

  
def yield_test():  
    first_value = yield 1  
    if first_value:  
        print 'first send is:' + first_value  
    second_value = yield 2  
    if second_value:  
        print 'second send is:' + second_value  
    third_value = yield 3  
    if third_value:  
        print 'third send is:' + third_value  
      
  
  
if __name__ == '__main__':  
    print  '*'*30 + 'test next' +  '*'*30  
    test_next = yield_test()  
    print test_next.next()  
    print test_next.next()  
    print test_next.next()  
    print  '*'*30 + 'test send' +  '*'*30  
    test_send = yield_test()  
    print test_send.next()  
    print test_send.next()  
    #send a value, that will continue from last yield  
    print test_send.send('first')  # begin code -- if second_value
    print  '*'*30 + 'test throw' +  '*'*30  
    test_throw = yield_test()  
    print test_throw.next()  
    #That will end all the generator  
    try:  
        test_throw.throw(GeneratorExit)  
    except GeneratorExit:  
        print 'GeneratorExit'  
    #call next or  send  again will stop  
    try:  
        test_throw.next()  
    except StopIteration:  
        print 'next StopIteration'  
    try:  
        test_throw.send('value')  
    except StopIteration:  
        print 'send StopIteration'  
    print  '*'*30 + 'test close' +  '*'*30  
    close_test = yield_test()  
    print close_test.next()  
    close_test.close()  
    #call next or  send  again will stop  
    try:  
        close_test.next()  
    except StopIteration:  
        print 'next StopIteration'  
    try:  
        close_test.send('value')  
    except StopIteration:  
        print 'send StopIteration'  