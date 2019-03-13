# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:41:23 2019

@author: surface
"""

#math
a = 824
b = 824824
print(b%7)
c = b/7
print(c)
d = c/11
print(d)
e = d/13
print(e)
#a=e. b=a×7×11×13

#Boolean
X = True
Y = False
Z = (Y and not X) or (X and not Y)
W = (X != Y)
print("same?", Z == W)
print("Z", Z)
X = False
Z = (Y and not X) or (X and not Y)
W = (X != Y)
print("same?", Z == W)
print("Z", Z)
Y = True
Z = (Y and not X) or (X and not Y)
W = (X != Y)
print("same?", Z == W)
print("Z", Z)
X = True
Z = (Y and not X) or (X and not Y)
W = (X != Y)
print("same?", Z == W)
print("Z", Z)
#Z is true if either X or Y (but not both) are true.
#Z and W are the same.