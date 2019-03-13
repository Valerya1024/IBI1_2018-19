# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:13:15 2019

@author: Valerya
"""

from random import randint
#select random integer n
n = randint(0,2**13)
#creat a string to store exponents
a = str(n)+' is '
#find the biggest power of 2 that is smaller than n
for i in range(13):
    #x as exponent
    x=12-i
    #if n is larger than 2**x, add x
    if n > 2**x:
        n = n - 2**x
        a+='2**'+str(x)+' + '
    #if n is smaller than 2**x, skip x
    #if n = 2**x, store x, end process
    elif n == 2**x:
        n=n-2**x
        a+='2**'+str(x)
print(a)