# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:15:04 2019

@author: surface
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b = 0.3; y = 0.05; T = 500
a = []
def chance(P,n):
    c = list(np.random.choice(range(2),n,p=[1-P,P]))
    return c.count(1)
for V in range(11):
    S = 9999
    S = int(S*(10-V)/10); I = 1; R = 0; N = S + I + R
    d = [I]
    for t in range (1,T):
        n = chance(y,I)
        m = chance(b*I/N,S)
        R += n
        I += m - n
        S -= m
        d.append(I)
    a.append(d)

a = pd.DataFrame(a)
a = a.T
a.columns = ['0','1','2','3','4','5','6','7','8','9','10']
a['t'] = np.linspace(0,T-1,T)
a.plot(x='t',y=['0','1','2','3','4','5','6','7','8','9','10'],label=['0','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'],figsize =(12,8))
plt.title('SIR vaccination model')
plt.ylabel('number of infected people')
plt.xlabel('time')
plt.legend(loc='upper right')
plt.show()
