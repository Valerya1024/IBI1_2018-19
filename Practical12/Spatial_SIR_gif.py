# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:50:58 2019

@author: Valerya
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anima
population = np.zeros((100,100)) #100x100 suscepticle population (=0)
b = 0.3; g = 0.05; T = 100 # b for beta, g for gamma
outbreak = np.random.choice(range(100),2) #select random person
population[outbreak[0],outbreak[1]] = 1 #random person infected (=1)
ims = []
if __name__ == "__main__":
    fig = plt.figure(figsize=(4,4), dpi=150)
    for t in range(T+1): #loop through T days
        infectedIndex = np.where(population==1) #locate the infected
         #plot heat map after 0,10,50,100 recursions
        im = plt.imshow(population, cmap='Blues_r', interpolation='nearest').findobj()
        ims.append(im)
        for i in range(len(infectedIndex[0])): #for all infectd points
            x = infectedIndex[0][i]
            y = infectedIndex[1][i] #obtain x,y coordinates
            for xNeighbour in range(x-1,x+2):
                for yNeighbour in range(y-1,y+2):
                    if (xNeighbour,yNeighbour) != (x,y): #for all 8 neighbours except himself
                        if xNeighbour not in [-1,100] and yNeighbour not in [-1,100]: #not fall off an edge
                            if population[xNeighbour,yNeighbour] == 0: # b probability the suscepticle infected (=1)
                                population[xNeighbour,yNeighbour] = np.random.choice(range(2),1,p=[1-b,b])[0]
                    else: #for himself, g probability he recovered (=2)
                        population[xNeighbour,yNeighbour] = np.random.choice(range(2),1,p=[1-g,g])[0] + 1
ani = anima.ArtistAnimation(fig, ims, interval=20, repeat_delay=20)
ani.save("Spatial_SIR.gif",writer='pillow')
