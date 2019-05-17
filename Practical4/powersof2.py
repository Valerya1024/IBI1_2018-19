# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:00:59 2019

@author: surface
"""

#there is no 2**13 limit.
n = 10086
#compute the binary of n.
X = bin(n)[2:]
#measure the length of X
l = len(X)
#store digits in a list
list = []
for i in range(l):
    if X[i] == "1":
        list.append("2**"+str(l - i - 1))   
#join the list to a string
print(n, "is", " + ".join(list))

# The maths in file powersof2.py is correct, but if a user just replaces the random number draw with the line n=1750, it does not work, because python expects a string. I don't understand, why you draw a random integer, convert it to string, and then convert it back to an integer again. It seems overly complicated and makes the code less robust to changes. It is possible that the solutions in the other files called something with powersof2 are correct, but I only looked in this one. It should not be up to the user to search for the file with the correct solution!
# origin: n = str(random number); X = bin(int(n,10)[2:]
# replaced random number; deleted str() and int()