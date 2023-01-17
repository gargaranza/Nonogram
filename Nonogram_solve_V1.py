from Outils import *
from Utilitaires_nonogram import *


def liste_correcte_old(Cases, Liste) :
        i = 0; k = 0
        for j in Cases :
                if j == -1 :
                        #print('Il y a des -1', Cases)
                        return False
        if list(Liste) == [0] and list(Cases) == ([0] * len(Cases)) :
                #print('Que des 0', Liste, Cases)
                return True
        
        while i < len(Cases) :
                if Cases[i] :
                        try :
                                if not(suite_correcte(Cases, i, Liste[k])) :
                                        #print('Suite trop petite', Cases, i, k)
                                        return False
                                try :
                                        if Cases[i + Liste[k]] :
                                                #print('Il y en a un de trop', Cases, Liste, k)
                                                return False
                                except IndexError : None
                                i += Liste[k]
                                k += 1
                        except IndexError :
                                #print('Trop de groupes', Liste, Cases)
                                return False
                else : i += 1
        if k < len(Liste) :
                #print('Pas assez de groupes', Liste, Cases)
                return False
        #print('Tout est bon', Liste, Cases)
        return True

def grille_correcte(G, Lignes, Colonnes) :
        for i, e in enumerate(Lignes) :
                if not(liste_correcte_old(ligne(G, i), e)) : return False
        for i, e in enumerate(Colonnes) :
                if not(liste_correcte_old(colonne(G, i), e)) : return False
        return True

def grille_coherante_old(G, Lignes, Colonnes, Lcorrecte, Ccorrecte) :
        for i in range(len(Lignes)) :
                if not(liste_coherante(ligne(G, i), Lcorrecte[i])) :
                        #print('Ligne {} : {}, {}'.format(i, ligne(G, i), Lignes[i]))
                        return False
        for i in range(len(Colonnes)) :
                if not(liste_coherante(colonne(G, i), Ccorrecte[i])) :
                        #print('Colonne {} : {}, {}'.format(i, colonne(G, i), Colonnes[i]))
                        return False
        return True


def solve(Lignes, Colonnes) :
        #if len(Lignes) == len(Colonnes) : taille = len(Lignes)
        #else : return False
        L = create_all_poss(Lignes,len(Colonnes))
        C = create_all_poss(Colonnes,len(Lignes))
        #I = [0] * len(Colonnes)
        G_1 = []

        #G_1 = lignes en cours d'étude possible
        for i in L[0] :
                #Tri des colonnes où il y a un 0
                for j in range(len(Colonnes)) :
                        if Colonnes[j] == (0,) and not(i[j]) : break
                G_1 += [[i]]

        
        
        #pour chaque ligne
        for i in range(1,len(Lignes)) :
                G = [j for j in G_1]
                G_1 = []
                #pour chaque possibilité des lignes précédentes
                for k in range(len(G)) :
                        #pour chaque possibilité de la ligne
                        for j in L[i] :
                                #Grille vide
                                P = [tuple([-1 for i in range(len(Colonnes))]) for j in range(len(Lignes))]
                                #On remplie le début de la Grille
                                for l in range(len(G[k])) :
                                        P[l] = G[k][l]
                                P[len(G[k])] = j

                                #on test si la ligne peut etre ajoutée
                                #print('P : {}\nLignes : {}\nColonnes : {}\nL : {}\nC : {}\n'.format(P,Lignes,Colonnes,L,C))
                                if grille_coherante_old(P, Lignes, Colonnes, L, C) :
                                        #On ajoute la ligne
                                        print(G[k] + [(j)])
                                        G_1 += [G[k] + [(j)]]

        G = []
        for i in G_1 :
                if grille_correcte(i, Lignes, Colonnes) :
                        G += [i]

        return G


