import math
import numpy as np

"""
Un élément a est un carré parfait si a = b² pour un élément dans le corps fini.
Pour déterminer quels éléments sont des carrés parfaits, on utilise des modulos.
On élève tous les éléments du corps F_n au carré et on vérifie si l'un de ces carrés modulo n est égal à 1.
"""

def quad_char(a,n): #déteriner si un élément est un carré parfait dans le corps fini ou non
    F_n = [i for i in range(n)] #corps fini de taille n 
    sq = [] #liste vide pour stocker les carrés 
    for i in range(len(F_n)): #on vérifie tous les éléments 
        sq.append(int(i**2)%n) #carrés modulos 7
    if a == 0:
        return 0
    if a in sq: #si a appartient à sq, c'est un carré parfait
        return 1 #le quadratic character est égal à 1
    else: 
        return -1 #sinon -1

"""
La matrice de Jacobsthal pour F_n est la matrice pour laquelle l'élément au rang i et à la colonne j est le quadratic character de j-i.
On la construit comme suivant:
"""

#focntion utilisée pour construire la matrice de jacobsthal
def jacob_matrix(n): #taille n donnée
    M_J = [] #liste vide
    for j in range(n): #boucle pour construire les n rangs
        row = [] #créer rang vide
        for i in range(n): #boucle pour construire chaque élément dans le rang (ce qui correspond à l'élément de chaque colonne)
            row.append(quad_char((j-i)%n,n)) #on ajoute chaque quadratic character au rang selon l'indice du rang - de la colonne modulo n
        M_J.append(row) #on ajoute chaque rang à la matrice
    return M_J

print(jacob_matrix(9)) #marche pour 7 mais pas pour 9? 

print(quad_char(1,9))


