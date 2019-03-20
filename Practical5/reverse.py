# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:10:59 2019

@author: surface
"""

str = "but soft what light in yonder window breaks"
str = str[::-1]
l = str.split()
l.sort(reverse=True)
print(l)
