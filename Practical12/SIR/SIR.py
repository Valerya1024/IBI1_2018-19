# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:15:04 2019

@author: surface
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
S = 9999; I = 1; R = 0; N = S + I + R; T = 500
b = 0.3; y = 0.05 #b for beta, y for gamma
a = [[9999,1,0,0]] #Day 0
def chance(P,n):
    c = list(np.random.choice(range(2),n,p=[1-P,P]))
    return c.count(1) #return the number of transformed people out of n people with probability P

for t in range (1,T+1): #loop through T days
    n = chance(y,I)  #people infected that day
    m = chance(b*I/N,S)  #people recovered that day
    R += n
    I += m - n
    S -= m
    a.append([S,I,R,t])
    
a = pd.DataFrame(a)
a.columns = ['S','I','R','t']
a.plot(x='t',y=['S','I','R'],label=['Suscepticle','Infected','Recovered'],figsize =(12,8))
plt.title('SIR model')
plt.ylabel('number of people')
plt.xlabel('time')
plt.legend(loc='upper right')
plt.savefig ('SIR' ,type='png')
plt.show()
