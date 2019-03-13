# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:13:15 2019

@author: surface
"""

from random import randint
#select random integer n
n = randint(1,2**13)
#store the origin integer in N
N = str(n)
#x as exponent
x = 13
#creat a list to store x
list = []
#find the biggest power of 2 that is smaller than n
for i in range(1,15):
    #if n is smaller than 2**x, skip x
    if n < 2**x:
        x = x - 1
    #if n is larger, store x
    elif n > 2**x:
        n = n - 2**x
        list.append("2**"+str(x))
        #next x
        x = x - 1
    #if n = 2**x, store x, end process
    else:
        list.append("2**"+str(x))
        break
#join the list to a string
print(N, "is", ' + '.join(list))