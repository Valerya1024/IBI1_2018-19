# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:05:51 2019

@author: surface
"""

hm_SOD = open('hm_SOD.txt').read()
ms_SOD = open('ms_SOD.txt').read()
rd_SOD = open('rd_SOD.txt').read()

def dis(Seq1,Seq2):
    edit_distance = 0
    for i in range(len(Seq1)):
        if Seq1[i] != Seq2[i]:
            edit_distance += 1
    print('\nedit_distance =',edit_distance)

x = input('Select function:\nA.SOD2_human,SOD2_mouse \nB.SOD2_human,random sequence \nC.SOD2_mouse,random sequence \nD.Input sequence\n')
if x == 'A':
    dis(hm_SOD,ms_SOD)
elif x == 'B':
    dis(hm_SOD,rd_SOD)
elif x == 'C':
    dis(ms_SOD,rd_SOD)
elif x == 'D':
    l1 = input('Sequence1:')
    l2 = input('Sequence2:')
    dis(l1,l2)
