# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:02:08 2019

@author: surface
"""

import itertools
L = input("Please input 4 numbers to compute 24:(use ',' to divide them)\n")
def compute(x,y,Op):
        if Op == '+': return x+y
        elif Op == '*': return x*y
        elif Op == '-': return x-y
        else: return x/y if y != 0 else None
if "." in L or "/" in L:
    print("The input number must be integers")
else:
    L = L.split(",")
    num = list(map(int,L))
    if len(num) != 4:
        print("Please try in file 24_n_digits.py" )
    elif max(num)>23 or min(num)<1:
        print("The input number must be integers from 1 to 23")
    else:
        sequence = list(itertools.permutations(num,4))[::]
        operations = ['+','-','*','/']
        op = list(itertools.combinations_with_replacement(operations,3))[::]
        operator = []
        for i in range(len(op)-1):
            operator += list(itertools.permutations(op[i],3))[::]
        operator = sorted(set(operator))
        x = y = 0
        for i in range(len(sequence)-1):
            if x == 0:
                S = sequence[i]
                for i in range(len(operator)-1):
                    O = operator[i]
                    if compute(compute(compute(S[0],S[1],O[0]),S[2],O[1]),S[3],O[2]) == 24:
                        x += 1
                        print("(("+str(S[0])+O[0]+str(S[1])+")"+O[1]+str(S[2])+")"+O[2]+str(S[3]))
                        break
                    elif compute(compute(S[0],S[1],O[0]),compute(S[2],S[3],O[2]),O[1]) == 24:
                        print("("+str(S[0])+O[0]+str(S[1])+")"+O[1]+"("+str(S[2])+O[2]+str(S[3])+")")
                        x += 1
                        break
                    else:
                        y += 1
        if x != 0:
            print("Yes")
        else:
            print("No")
        print("Recursion times:"+str(y+1))
        