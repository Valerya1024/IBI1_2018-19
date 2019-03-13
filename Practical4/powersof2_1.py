# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:13:15 2019

@author: surface
"""

from random import randint
#select random integer n, store the initial value in m
n = m = randint(1,2**13)
#x as exponent
#creat a list to store x
list = []
#find the biggest power of 2 that is smaller than n
for x in range(12,-1,-1):
    #if n is smaller than 2**x, skip x
    #if n is larger, store x
    if  n > 2**x:
        list.append("2**"+str(x))
        n = n - 2**x
    #if n = 2**x, print x, end process
    elif n == 2**x:
        n = n - 2**x
        list.append("2**"+str(x))
#join the list to a string
print(str(m), "is", ' + '.join(list))