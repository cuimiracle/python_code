import sys
try:
    sys.exit(1)
except SystemExit, e:
    print 'e:'
    print e
    print 'SystemExit:'
    print SystemExit