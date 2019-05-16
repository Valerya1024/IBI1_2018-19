# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:13:15 2019

@author: surface
"""

#This code is additional, never grade it
from random import randint
n = m = randint(1,2**13)
list = []
for x in range(12,-1,-1):
    if  n > 2**x:
        list.append("2**"+str(x))
        n = n - 2**x
    elif n == 2**x:
        n = n - 2**x
        list.append("2**"+str(x))
print(str(m), "is", ' + '.join(list))