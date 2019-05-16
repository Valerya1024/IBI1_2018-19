# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:27:52 2019

@author: Valerya

This is not the file required, never grade it
EXAMPLE
[13.0, 12.0, 4.0, 10.0]
Please choose 2 numbers above to do calculation:
12-4
[13.0, 10.0, 8.0]
Please choose 2 numbers above to do calculation:
13-8
[10.0, 5.0]
Please choose 2 numbers above to do calculation:
undo
[13.0, 12.0, 4.0, 10.0]
Please choose 2 numbers above to do calculation:
12-4
[13.0, 10.0, 8.0]
Please choose 2 numbers above to do calculation:
13-10
[8.0, 3.0]
Please choose 2 numbers above to do calculation:
8*3
24! Total time = 58
"""


import random
import re
import time
import fractions
import itertools

def compute(x,y,Op):
    if x == None or y == None:
        return None
    else:
        if Op == '+': return x+y
        elif Op == '*': return x*y
        elif Op == '-': return x-y
        else: return fractions.Fraction(x,y) if y != 0 else None
def calculation(operation):
        if operation[1] == '+': return float(operation[0])+float(operation[2])
        elif operation[1] == '-': return float(operation[0])-float(operation[2])
        elif operation[1] == '*': return float(operation[0])*float(operation[2])
        elif operation[1] == '/' and operation[2] != 0: return float(operation[0])/float(operation[2])
        else: 
            print("Invalid calculation") 
            return None

x = 0
while x == 0:
    a = random.randint(1,13)
    b = random.randint(1,13)
    c = random.randint(1,13)
    d = random.randint(1,13)
    num = [a,b,c,d]
    sequence = list(itertools.permutations(num,4))[::]
    operations = ['+','-','*','/']
    op = list(itertools.combinations_with_replacement(operations,3))[::]
    operator = []
    ans = ''
    for i in range(len(op)-1):
        operator += list(itertools.permutations(op[i],3))[::]
    operator = sorted(set(operator))
    for i in range(len(sequence)-1):
        if x == 0:
            S = sequence[i]
            for i in range(len(operator)-1):
                O = operator[i]
                if compute(compute(compute(S[0],S[1],O[0]),S[2],O[1]),S[3],O[2]) == 24.0:
                    x = 1
                    ans = "(("+str(S[0])+O[0]+str(S[1])+")"+O[1]+str(S[2])+")"+O[2]+str(S[3])
                    break
                elif compute(compute(S[0],S[1],O[0]),compute(S[2],S[3],O[2]),O[1]) == 24.0:
                    ans = "("+str(S[0])+O[0]+str(S[1])+")"+O[1]+"("+str(S[2])+O[2]+str(S[3])+")"
                    x = 1
                    break
                elif compute(compute(S[0],compute(S[1],S[2],O[1]),O[0]),S[3],O[2]) == 24.0:
                    ans = "("+str(S[0])+O[0]+"("+str(S[1])+O[1]+str(S[2])+"))"+O[2]+str(S[3])
                    x = 1
                    break
                elif compute(S[0],compute(S[1],compute(S[2],S[3],O[2]),O[1]),O[0]) == 24.0:
                    ans = str(S[0])+O[0]+"("+str(S[1])+O[1]+"("+str(S[2])+O[2]+str(S[3])+"))"
                    x = 1
                    break
                elif compute(S[0],compute(compute(S[1],S[2],O[1]),S[3],O[2]),O[0]) == 24.0:
                    ans = str(S[0])+O[0]+"(("+str(S[1])+O[1]+str(S[2])+")"+O[2]+str(S[3])+")"
                    x = 1
                    break

start_time = time.time()
while len(num)>1:
    num = list(map(float,num))
    print(num)
    operation = re.split(r'([-\+*/])',input("Please choose 2 numbers above to do calculation:\n"))
    if operation == ['undo']:
        num = list(map(float,[a,b,c,d]))
    elif float(operation[0]) in num and float(operation[2]) in num:
        num.remove(float(operation[0]))
        num.remove(float(operation[2]))
        num.append(calculation(operation))
    else:
        print("Invalid calculation")
if num[0] == 24:
    end_time = time.time()
    print("24! Total time =", int(end_time-start_time))
else:
    print("try again!"+ans)
    
