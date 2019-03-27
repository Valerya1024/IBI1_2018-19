# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:22:30 2019

@author: surface
"""

from matplotlib import pyplot as plt
DNA = input("Give me a sequence of DNA:")
A = DNA.count("A", 0, len(DNA))
G = DNA.count("G", 0, len(DNA))
C = DNA.count("C", 0, len(DNA))
T = len(DNA) - A - G - C
Dict = {"A":A,"G":G,"C":C,"T":T}
print(Dict)
sizes = [A,G,C,T]
labels = ["A","G","C","T"]
colors='yellowgreen','gold','lightskyblue','lightcoral'
plt.title("pie of the four DNA neucleotides")
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')