# -*- coding:utf-8 -*-
import unittest
import __future__

def add(x,y):
    return x+y
#    raise NotImplementedError('sth')
#    if(isinstance(x,set) and (isinstance(y,set))):
#        return x|y
    
class ATest(unittest.TestCase):
    def testAddInt(self):
        expValue = 8
        retValue = add(3,5)
        self.assertEqual(expValue, retValue)
        
    def testAddSet(self):
        self.skipTest("Skip due to Bug #134562")
        expValue = set("012343456")
        retValue = add(set("01234"),set("3456"))
        self.assertEqual(expValue, retValue)
        
    def testAddTypeError(self):
        #是否报了TypeError异常
        self.assertRaises(TypeError,add,3,"hello")
        
    
if __name__ == "__main__":
    unittest.main()


    