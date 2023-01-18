from Utilitaires_nonogram import *


#On vérifie la cohérence de la grille par ligne
def grille_coherante_L(G, nLignes, All_lignes_possible):
        for i in range(nLignes):
                if not(liste_coherante(ligne(G, i), All_lignes_possible[i])):
                        return False
        return True

#On vérifie la cohérence de la grille par colonne
def grille_coherante_C(G, nColonnes, All_colonnes_possible):
        for i in range(nColonnes):
                if not(liste_coherante(colonne(G, i), All_colonnes_possible[i])):
                        return False
        return True


def solve(Lignes, Colonnes, bis=False, v=0):

        #fonction qui calcule le nombre de possibilitées pour chaque contraintes et qui retourne ce nombre (p), l'indice de la colonne/liste (i) et la liste elle-même (e)
        def info(Liste, taille):
                Liste_info = []
                Sum = 0
                for i, e in enumerate(Liste) :
                        if e == (0,) : p = 1
                        else : p = Cnk(taille - sum(e) + 1 - len(e), taille - sum(e) + 1)                       #Formule qui compte nombre de possibilitées pour la contrainte (Cnk : combinaison de k parmis n)
                        Liste_info += [(p, i, e)]
                        Sum += p
                Liste_info = sorted(Liste_info)                                                                 #On renvoie la liste ordonnée par nombre de possibilitées
                return Liste_info, Sum

        def main_branch(Liste, taille_1, taille_2, Liste_infos, change, grille_coherante):
                all_poss = (create_all_poss_bis if bis else create_all_poss)                                    #La fonction change en fonction du bis
                
                G = [[[-1 for i in range(len(Colonnes))] for j in range(len(Lignes))]]                          #Grille vide
                All_listes_possible = all_poss(Liste,taille_1)                                                  
                for rangee in Liste_infos:
                        if v: print('rangee', rangee)
                        G_poss = G
                        G = []
                        L = all_poss((rangee[2],),taille_2)[0]
                        if v > 1: print('(G){}*{}(L)={}'.format(len(G_poss), len(L), len(G_poss)*len(L)))
                        for g in G_poss :                                                                       #Pour chaque gille encore possible
                                for l in L :                                                                    #Pour chaque liste possible
                                        G_1 = change(g, rangee[1], l)                                           #On change la ligne
                                        if grille_coherante(G_1, taille_1, All_listes_possible):                #Puis on regarde si c'est cohérent
                                                G += [G_1]
                return G

        
        nLignes = len(Colonnes)
        nColonnes = len(Lignes)

        Lignes_info,sumL = info(Lignes, nLignes)
        Colonnes_info,sumC = info(Colonnes, nColonnes)
        
        if sumL < sumC :
                G = main_branch(Colonnes, nColonnes, nLignes, Lignes_info, change_ligne, grille_coherante_C)
        else :
                G = main_branch(Lignes, nLignes, nColonnes, Colonnes_info, change_colonne, grille_coherante_L)
                
        return G


