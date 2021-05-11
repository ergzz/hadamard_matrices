import math
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random

import sylvester as syl

def correctLine(c,n): #on rentre une "lettre" c et sa taille n
    H_n = syl.hadamard(n) #créer la matrice d'Hadamard de taille n
    d = list(c.dot(H_n)) #produit entre la matrice et la lettre sous forme de liste
    dMax = max(d, key=abs) #élément en valeur absolue
    dMaxIndex = d.index(dMax) #trouver l'index de la valeur absolue max
    hamming = n/2 #permet de déterminer la capacité de correction maximum
    if abs(dMax) == hamming: #impossible à corriger dans ce cas : la ligne est composée de 0 et de +- n/2
        return "Trop ambigu pour corriger"
    else: 
        return chr(int(dMaxIndex)) #version améliorée : se base sur l'indice, peu importe le signe de dMax 

def brouille(l,n): #brouille une liste en n endroits
    for i in range(n): 
        l[random.randint(0,len(l)-1)] = random.choice([-1,1])
    return l

def convertLetter(l): #convertir un message de ascii en ligne de la matrice H_128
    H_128 = syl.hadamard(128) #matrice 128
    return np.array(H_128[ord(l)])


def correctMessage(m): #utilise le correct line sur un message entier
    for char in m: 
        print(correctLine(brouille(convertLetter(char),75), 128))

print(correctMessage("Bonjour a tous"))

