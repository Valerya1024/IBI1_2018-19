# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:13:15 2019

@author: Valerya
"""

from random import randint
#select random integer n
n = randint(1,2**13)
#print the origin integer
print(str(n), "is", end=" ")
#x as exponent
#find the biggest power of 2 that is smaller than n
for x in range(12,-1,-1):
    #if n is smaller than 2**x, skip x
    #if n is larger, print x
    if n > 2**x:
        n = n - 2**x
        print("2**"+str(x)+" + ", end="")
    #if n = 2**x, print x, end process
    elif n == 2**x:
        print("2**"+str(x))
        break
