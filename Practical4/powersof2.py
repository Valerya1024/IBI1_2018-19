# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:00:59 2019

@author: surface
"""

import random

#select random integer n
n = str(random.randint(1,8192))
print("n =", n)
#compute the binary of n
X = bin(int(n,10))[2:]
print(X)
#measure the length of X
l = len(X)
#store digits in a list
list = []

for i in range(l):
    if X[i] == "1":
        list.append("2**"+str(l - i - 1))
        
#join the list to a string
print(n, "is", " + ".join(list))