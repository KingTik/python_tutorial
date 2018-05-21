'''
difference between range and xrange in python 2.7

range returns array but xrange returs object that yields values
it is best to use with large numbers
'''

import time

start = time.time()
for i in range(10000000): #10M
    pass
stop = time.time()


print stop - start

start = time.time()
for i in xrange(10000000): #10M
    pass
stop = time.time()


print stop - start

