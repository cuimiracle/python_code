aaa = '100'
def testFun():
    apple = 3
    pear = 5
    return locals()

# print locals()
testlocal = testFun()
print testlocal
# print testlocal['pear']