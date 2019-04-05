# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:02:08 2019

@author: Valerya, inspired by yangjiaolei
"""

from fractions import Fraction
L = input("Please input numbers to compute 24:(use ',' to divide them)\n")
if "." in L or "/" in L:
    print("The input number must be integers")
else:
    L = L.split(",")
    num = list(map(int,L))
    if max(num)>23 or min(num)<1:
        print("The input number must be integers from 1 to 23")
    else:
        times = 0
        def cal(n):
            global times
            times += 1
            if n == 1:
                if float(num[0]) == 24:
                    return 1
                else:
                    return 0
            else:
                for i in range(n):
                    for j in range(i+1,n):
                        a = num[i]
                        b = num[j]
                        num[j] = num[n-1]
                    
                        num[i] = a+b
                        if cal(n-1):
                            return 1
                        num[i] = a-b
                        if cal(n-1):
                            return 1
                    
                        num[i] = b-a
                        if cal(n-1):
                            return 1
                    
                        num[i] = a*b
                        if cal(n-1):
                            return 1
                        if a != 0:
                            num[i] = Fraction(b,a)
                            if cal(n-1):
                                return 1
                        if b != 0:
                            num[i] = Fraction(a,b)
                            if cal(n-1):
                                return 1
                        num[i] = a
                        num[j] = b
            return 0
    
        if cal(len(num)):
            print("Yes")
        else:
            print("No")
        print("Recursion times:"+str(times))