import math
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import sylvester as syl

def correctLine(c,n): #on rentre une "lettre" c et sa taille n
    H_n = syl.hadamard(n) #créer la matrice d'Hadamard de taille n
    d = c.dot(H_n) #produit entre la matrice et la lettre
    dMax = max(d.max(), d.min(), key=abs) #élément en valeur absolue
    dMaxIndex = np.where(d == abs(dMax))[1] #trouver l'index du max ou du min 
    hamming = n/2 #permet de déterminer la capacité de correction 
    if abs(dMax) == hamming: #impossible à corriger dans ce cas
        print("Trop ambigu pour corriger")
    elif dMax > 0: 
        #print(H_n[dMaxIndex]) #retourne la ligne correspondante si indice positif
        print(chr(int(dMaxIndex)))
    elif dMax < 0:
        #print(np.negative(H_n[dMaxIndex])) #opposé si indice négatif
        print(chr(int(dMaxIndex)))


def convertMessage(m): #convertir un message de ascii en ligne de la matrice H_128
    H_128 = syl.hadamard(128) #matrice 128
    convertedMessage = [] #message 
    for letter in m: 
        convertedMessage.append(H_128[ord(letter)]) #ajoute la ligne correspondant au charactère ascii
    return np.array(convertedMessage)


def correctMessage(m): #utilise le correct line sur un message entier
    for char in m: 
        correctLine(convertMessage(char), 128)

correctMessage("He")
