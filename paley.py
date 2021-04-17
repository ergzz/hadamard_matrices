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
    if a%n == 0:
        return 0
    if a%n in sq: #si a appartient à sq, c'est un carré parfait
        return 1 #le quadratic character est égal à 1
    else: 
        return -1 #sinon -1

"""
La matrice de Jacobsthal pour F_n est la matrice pour laquelle l'élément au rang i et à la colonne j est le charactère quadratique de j-i.
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
    return np.array(M_J)


#marche uniquement pour les nbs premiers mais pas les puissances d'un premier impair? ex 9 ne fonctionne pas 
#pour 9 sur wikipedia : utilisation d'une extension avec mipo mais comment procéder ici?

def paley2(i):
    A = np.zeros((2,2), int)
    if i==1: 
        A = np.array([[1,1],[1,-1]])
    elif i == -1:
        A = np.array([[-1,-1],[-1,1]])
    elif i == 0:
        A = np.array([[1,-1],[-1,-1]])
    return A

def hadamard(n): #définir matrice Hadamard
    H = np.zeros((n,n),int) #créer matrice vide
    I = np.identity(n,int) #créer matrice identité
    if (n-1)%4 == 3: #Paley 1 : si n-1 == 3 mod 4, on crée une matrice de taille n
        H = I + np.block([[0, np.ones(n-1)], [np.full((n-1,1), -1), jacob_matrix(n-1)]]) #matrice par blocs
        return(np.array(H)) #matrice construite
    if (n-1)%4 == 1: #Paley 2
        H_2 = np.block([[0, np.ones(n-1)], [np.full((n-1,1), 1), jacob_matrix(n-1)]])
        H_2 = np.vstack(np.hstack(paley2(H_2[j][i]) for i in range(n)) for j in range(n)) #construction matrice par for loop avec vstack et hstack
        return(np.array(H_2))


#print(hadamard(8))
#print(hadamard(12))
