# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:00:59 2019

@author: surface
"""

from random import randint
#select random integer n
n = str(randint(1,8192))
print("n =", n)
#compute the binary of n
X = bin(int(n,10))[2:]
#measure the length of X
l = len(X)
#store digits in a list
list = []
m = 0
for i in range(1,l + 1):
    if X[m] == "1":
        list.append("2**"+str(l - 1))
        m = m + 1
        l = l - 1
    else:
        m = m + 1
        l = l - 1
#join the list to a string
print(n, "is", " + ".join(list))