# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:02:08 2019

@author: Valerya
"""

import itertools
from fractions import Fraction
L = input("Please input 4 numbers to compute 24:(use ',' to divide them)\n")
def compute(x,y,Op):
    if x == None or y == None:
        return None
    else:
        if Op == '+': return x+y
        elif Op == '*': return x*y
        elif Op == '-': return x-y
        else: return Fraction(x,y) if y != 0 else None
if "." in L or "/" in L:
    print("The input number must be integers")
else:
    L = L.split(",")
    num = list(map(int,L))
    if len(num) != 4:
        print("Please try in file 24_n_digits.py" )
    elif max(num)>13 or min(num)<1:
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
                    if compute(compute(compute(S[0],S[1],O[0]),S[2],O[1]),S[3],O[2]) == 24.0:
                        x += 1
                        print("(("+str(S[0])+O[0]+str(S[1])+")"+O[1]+str(S[2])+")"+O[2]+str(S[3]))
                        break
                    elif compute(compute(S[0],S[1],O[0]),compute(S[2],S[3],O[2]),O[1]) == 24.0:
                        print("("+str(S[0])+O[0]+str(S[1])+")"+O[1]+"("+str(S[2])+O[2]+str(S[3])+")")
                        x += 2
                        break
                    elif compute(compute(S[0],compute(S[1],S[2],O[1]),O[0]),S[3],O[2]) == 24.0:
                        print("("+str(S[0])+O[0]+"("+str(S[1])+O[1]+str(S[2])+"))"+O[2]+str(S[3]))
                        x += 3
                        break
                    elif compute(S[0],compute(S[1],compute(S[2],S[3],O[2]),O[1]),O[0]) == 24.0:
                        print(str(S[0])+O[0]+"("+str(S[1])+O[1]+"("+str(S[2])+O[2]+str(S[3])+"))")
                        x += 4
                    elif compute(S[0],compute(compute(S[1],S[2],O[1]),S[3],O[2]),O[0]) == 24.0:
                        print(str(S[0])+O[0]+"(("+str(S[1])+O[1]+str(S[2])+")"+O[2]+str(S[3])+")")
                        x += 5
                    else:
                        y += 5
        if x != 0:
            print("Yes")
        else:
            print("No")
        print("Recursion times:"+str(y+5))
        