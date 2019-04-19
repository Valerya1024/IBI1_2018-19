# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:13:15 2019

@author: Valerya
"""

#This code is additional, never grade it.
from random import randint
n = randint(0,2**13)
a = str(n)+' is '
for i in range(13):
    x=12-i
    if n >= 2**x:
        n = n - 2**x
        a+='2**'+str(x)+' + '
    b = a[:-3]
print(b)