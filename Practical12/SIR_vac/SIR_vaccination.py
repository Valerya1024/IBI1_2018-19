# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:15:04 2019

@author: surface
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b = 0.3; y = 0.05; T = 1000 # b for beta, y for gamma
a = []
def chance(P,n):
    c = list(np.random.choice(range(2),n,p=[1-P,P]))
    return c.count(1) #return the number of transformed people out of n people with probability P
for V in range(11): #loop through 11 different vaccination rates
    S = int(9999*(10-V)/10); I = 1; R = 0; N = 10000 #vaccinated people excluded in S
    d = [I] #Day 0
    for t in range (1,T+1): #loop through T Days
        n = chance(y,I) #people infected that day
        m = chance(b*I/N,S) #people recovered that day
        R += n
        I += m - n
        S -= m
        d.append(I)
    a.append(d)

a = pd.DataFrame(a)
a = a.T #rotation
a.columns = ['0','1','2','3','4','5','6','7','8','9','10']
a['t'] = np.linspace(0,T,T+1)
a.plot(x='t',y=['0','1','2','3','4','5','6','7','8','9','10'],label=['0','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'],figsize =(12,8))
plt.title('SIR model with different vaccination rates')
plt.ylabel('number of infected people')
plt.xlabel('time')
plt.legend(loc='upper right')
plt.savefig ('SIR vaccination model' ,type='png')
plt.show()
