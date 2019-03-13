# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:13:15 2019

@author: Valerya
"""

from random import randint
#select random integer n
n = randint(1,2**13)
#print the origin integer
#one UIUC guy taught me to print in the same line with end=
print(n, "is", end=" ")
#x as exponent
x = 13
#find the biggest power of 2 that is smaller than n
for i in range(1,15):
    #if n is smaller than 2**x, skip x
    if n < 2**x:
        x = x - 1
    #if n is larger, print x
    elif n > 2**x:
        n = n - 2**x
        print("2**"+str(x)+" + ", end="")
        #next x
        x = x - 1
    #if n = 2**x, print x, end process
    else:
        print("2**"+str(x))
        break
