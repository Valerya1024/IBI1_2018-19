# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:02:08 2019

@author: surface
"""

import time
time_start=time.time()
import itertools
import re
def compute(x,y,Op):
    if Op=='+':return x+y
    elif Op=='*':return x*y
    elif Op=='-':return x-y
    else:return x/y if y != 0 else None
L = re.split(r',',input("Please input 4 numbers to compute 24:(use ',' to divide them)"))
for i in range(len(L)):
    L[i] = int(L[i])
if max(L)>23 or min(L)<1:
    print("The input number must be integers from 1 to 23")
else:
    sequence = list(itertools.permutations(L,4))[::]
    operations = ['+','-','*','/']
    op = list(itertools.combinations_with_replacement(operations,3))[::]
    operator = []
    for i in range(len(op)-1):
        operator += list(itertools.permutations(op[i],3))[::]
    x = 0
    for i in range(len(sequence)-1):
            S = sequence[i]
            for i in range(len(operator)-1):
                O = operator[i]
                a = compute(S[0],S[1],O[0])
                b = compute(a,S[2],O[1])
                c = compute(S[2],S[3],O[2])
                if compute(b,S[3],O[2]) == 24:
                    x += 1
                    break
                elif compute(a,c,O[1]) == 24:
                    x += 1
                    break
                else:
                    x += 0
    if x != 0:
        print("Yes")
    else:
        print("No")
    time_end=time.time()
    print("Recursion times:", int((time_end-time_start)*100))
        