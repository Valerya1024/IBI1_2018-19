# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:17:28 2019

@author: surface
"""

#Collatz sequence
#define n as a random positive integer
#here we only consider the simplified cases when n <= 100
import random as rd
n = 0
n = rd.randint(1,100)
print("origin n =", n)
while n != 1:
    #when n is even
    if n%2 == 0:
        #the next number is n divided by 2
        n = n/2
        print("n is even and next n =", n)
    #when n is odd
    else:
        #the next number is 3n + 1
        n = 3*n + 1
        print("n is odd and next n =", n)
print("then the sequence ends with 4−2−1−4−2−1−4−2−1−...")