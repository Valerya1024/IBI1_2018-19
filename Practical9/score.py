# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:11:12 2019

@author: surface
"""

import pandas
def score(a,b):
    f = open('BLOSUM62.txt','r').read()
    f = f.split('\n')
    score = []
    for s in f:
        s = s.split(',')
        s = list(map(int,s))
        score.append(s)
    Dict = {'A':0, 'R':1, 'N':2, 'D':3, 'C':4, 'Q':5, 'E':6, 'G':7, 'H':8, 'I':9, 'L':10, 'K':11, 'M':12, 'F':13, 'P':14, 'S':15, 'T':16, 'W':17, 'Y':18, 'V':19, 'B':20, 'Z':21, 'X':22, '*':23}
    a = Dict[a]
    b = Dict[b]
    return score[a][b]

hm_SOD = open('hm_SOD.txt').read()
ms_SOD = open('ms_SOD.txt').read()
rd_SOD = open('rd_SOD.txt').read()

def BLAST(SeqA,SeqB):
    LA = []
    Ld = []
    LB = []
    AA = list(range(1,len(SeqA)+1))
    identity = 0
    final_score = 0
    for i in range(len(SeqA)):
        final_score += score(SeqA[i],SeqB[i])
        LA.append(SeqA[i])
        LB.append(SeqB[i])
        if SeqA[i] != SeqB[i]:
            if final_score >= 0:
                Ld.append('+')
            else:
                Ld.append(' ')
        else:
            identity += 1
            Ld.append(SeqA[i])

    alignment = pandas.DataFrame({'Query':LA, ' ':Ld, 'Sbjct':LB, 'AA':AA})
    alignment = alignment.set_index('AA')
    alignment = alignment.T
    pandas.set_option('display.max_columns', None)
    print('Score:',final_score)
    print('Score per amino acid:',final_score/len(SeqA))
    print('Percentage identity: '+str(100*identity/len(SeqB))+'%')
    print(alignment)

x = input('Select function:\nA.SOD2_human,SOD2_mouse \nB.SOD2_human,random sequence \nC.SOD2_mouse,random sequence \nD.Input sequence\n')   
if x == 'A':
    print('\nQuery: SOD2_human (NP_000627.2)\nSbjct:SOD2_mouse (NP_038699.2)\n')
    BLAST(hm_SOD,ms_SOD)
elif x == 'B':
    print('\nQuery: SOD2_human (NP_000627.2)\nSbjct: a random sequence\n')
    BLAST(hm_SOD,rd_SOD)
elif x == 'C':
    print('\nQuery: SOD2_mouse (NP_038699.2)\nSbjct: a random sequence\n')
    BLAST(ms_SOD,rd_SOD)
elif x == 'D':
    l1 = input('Query: (id:sequence)\n')
    l2 = input('Sbjct: (id:sequence)\n')
    l1 = l1.split(':')
    l2 = l2.split(':')
    print('\nQuery: '+l1[0]+'\nSbjct: '+l2[0])
    BLAST(l1[1],l2[1])
