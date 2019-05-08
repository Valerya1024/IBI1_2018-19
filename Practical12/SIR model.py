# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:15:04 2019

@author: surface
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
S = 9999; I = 1; R = 0; N = S + I + R; T = 500
b = 0.3; y = 0.05
a = [[9999,1,0,0]]
def chance(P,n):
    c = list(np.random.choice(range(2),n,p=[1-P,P]))
    return c.count(1)

for t in range (1,T):
    n = chance(y,I)
    m = chance(b*I/N,S)
    R += n
    I += m - n
    S -= m
    a.append([S,I,R,t])
    
a = pd.DataFrame(a)
a.columns = ['S','I','R','t']
a.plot(x='t',y=['S','I','R'],label=['Suscepticle','Infected','Recovered'],figsize =(12,8))
plt.title('SIR vaccination model')
plt.ylabel('number of people')
plt.xlabel('time')
plt.legend(loc='upper right')
plt.show()
