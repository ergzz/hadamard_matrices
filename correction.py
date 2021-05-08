import math
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import sylvester as syl

#test
M = np.array(syl.hadamard(8))
c = np.array([1,-1,-1,1,1,1,1,1])

d1 = c.dot(M)
dmax1 = list(d1).index(max(d1, key=abs))

# print(d1)
# print(dmax1)
# fin test

def correctLine(c,n): #on rentre une "lettre" c et sa taille n
    H_n = np.array(syl.hadamard(n)) #créer la matrice d'Hadamard de taille n
    d = c.dot(H_n) #produit entre la matrice et la lettre
    dMax = max(d, key=abs)
    dMaxIndex = list(d).index(max(d, key=abs)) #index maximum en valeur absolue
    hamming = n/2 #permet de déterminer la capacité de correction 
    if abs(dMax) == hamming: #impossible à corriger dans ce cas
        return "Trop ambigu pour corriger"
    elif dMax > 0: 
        return H_n[dMaxIndex]
    elif dMax < 0:
        return -H_n(dMaxIndex)

print(correctLine(c,8))