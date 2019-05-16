# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:13:15 2019

@author: Valerya
"""

#This code is additional, never grade it
from random import randint
n = randint(1,2**13)
print(str(n), "is", end=" ")
for x in range(12,-1,-1):
    if n > 2**x:
        n = n - 2**x
        print("2**"+str(x)+" + ", end="")
    elif n == 2**x:
        print("2**"+str(x))
        break
