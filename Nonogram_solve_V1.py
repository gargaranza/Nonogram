from Utilitaires_nonogram import *


#On vérifie si les Cases respectent la liste de contraintes
def liste_correcte_old(Cases, Liste) :
        i = 0; k = 0
        
        for j in Cases :
                if j == -1 :                                                            #Si on trouve des -1, la grille n'est pas finie
                        return False
        if list(Liste) == [0] and list(Cases) == ([0] * len(Cases)) :                   #On vérifie la contrainte 0
                return True
        
        while i < len(Cases) :
                if Cases[i] :                                                           #On ignore les 0
                        try :
                                if not(suite_correcte(Cases, i, Liste[k])) :            #On vérifie si la série de 1 est assez longue
                                        return False
                                try :
                                        if Cases[i + Liste[k]] :                        #On vérifie si la série de 1 n'est pas trop longue
                                                return False
                                except IndexError : None
                                i += Liste[k]
                                k += 1
                        except IndexError :                                             #On a respecté toutes les contraintes et il reste des 1
                                return False
                else : i += 1
        if k < len(Liste) :                                                             #On vérifie si on a respecté toutes les contraontes
                return False
        return True

#La grille est correcte si toues les lignes et colonnes sont correctes
def grille_correcte(G, Lignes, Colonnes) :
        for i, e in enumerate(Lignes) :
                if not(liste_correcte_old(ligne(G, i), e)) : return False
        for i, e in enumerate(Colonnes) :
                if not(liste_correcte_old(colonne(G, i), e)) : return False
        return True

#La grille est cohérente si toues les lignes et colonnes sont cohérentes
def grille_coherante_old(G, Lignes, Colonnes, Lcorrecte, Ccorrecte) :
        for i in range(len(Lignes)) :
                if not(liste_coherante(ligne(G, i), Lcorrecte[i])) : return False
        for i in range(len(Colonnes)) :
                if not(liste_coherante(colonne(G, i), Ccorrecte[i])) : return False
        return True


def solve(Lignes, Colonnes, v=0) :
        L = create_all_poss(Lignes,len(Colonnes))
        C = create_all_poss(Colonnes,len(Lignes))
        
        G_1 = []                                                                        #G_1 : lignes en cours d'étude possible

        
        for i in L[0] :                                                                 #Premier tri des colonnes '0'
                for j in range(len(Colonnes)) :
                        if Colonnes[j] == (0,) and not(i[j]) : break
                G_1 += [[i]]

        
        
        #Pour chaque ligne
        for i in range(1,len(Lignes)) :
                G = [j for j in G_1]
                G_1 = []
                #Pour chaque possibilité des lignes précédentes
                for k in range(len(G)) :
                        #Pour chaque possibilité de la ligne
                        for j in L[i] :
                                #Grille vide
                                P = [tuple([-1 for i in range(len(Colonnes))]) for j in range(len(Lignes))]
                                #On remplie le début de la Grille
                                for l in range(len(G[k])) :
                                        P[l] = G[k][l]
                                P[len(G[k])] = j

                                #On test si la ligne peut etre ajoutée
                                if grille_coherante_old(P, Lignes, Colonnes, L, C) :
                                        #On ajoute la ligne
                                        if v:print(G[k] + [(j)])
                                        G_1 += [G[k] + [(j)]]

        G = []
        for i in G_1 :
                if grille_correcte(i, Lignes, Colonnes) :
                        G += [i]

        return G


