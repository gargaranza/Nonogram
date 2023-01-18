from Utilitaires_nonogram import *


#On vérifie la cohérence de la liste (ligne/colonne) 
def liste_coherante_bis(Cases_fixees, Listes_possibles):
        for i, liste in enumerate(Listes_possibles, 1):
                if coherant(liste, Cases_fixees):
                    return i
        return False

#On vérifie la cohérence de la grille par ligne et on renvoie la liste des possibilitées sans celles impossible
def grille_coherante_L(G, nLignes, All_lignes_possible):
        All_lignes_possible_copie = [a[:] for a in All_lignes_possible] 
        for i in range(nLignes):
                c = liste_coherante_bis(ligne(G, i), All_lignes_possible_copie[i])
                if not c:
                        return False
                else:
                    All_lignes_possible_copie[i] = tuple(list(All_lignes_possible_copie[i])[c-1:])
        return All_lignes_possible_copie

#On vérifie la cohérence de la grille par colonne
def grille_coherante_C(G, nColonnes, All_colonnes_possible):
        All_colonnes_possible_copie = [tuple([e for e in a]) for a in All_colonnes_possible]
        for i in range(nColonnes):
                c = liste_coherante_bis(colonne(G, i), All_colonnes_possible_copie[i])
                if not c:
                        return False
                else:
                    All_colonnes_possible_copie[i] = tuple(list(All_colonnes_possible_copie[i])[c-1:])
        return All_colonnes_possible_copie
    


def solve(Lignes, Colonnes, v=0):

        #même que V2
        def info(Liste, taille):
                Liste_info = []
                Sum = 0
                for i, e in enumerate(Liste):
                        if e == (0,) : p = 1
                        else : p = Cnk(taille - sum(e) + 1 - len(e), taille - sum(e) + 1)
                        Liste_info += [(p, i, e)]
                        Sum += p
                Liste_info = sorted(Liste_info)
                return Liste_info, Sum

        def main_branch(Liste, taille_1, taille_2, Liste_infos, change, grille_coherante):
                All_listes_possible = create_all_poss_bis(Liste,taille_1)
                G = [([[-1 for i in range(len(Colonnes))] for j in range(len(Lignes))], All_listes_possible)]   #La "grille" est composée de la grille + l'ensemble des lignes/colonnes possibles (qui réduit avec le temps)
                for rangee in Liste_infos:
                        if v: print('rangee', rangee)
                        G_poss = G
                        G = []
                        L = create_all_poss_bis((rangee[2],),taille_2)[0]
                        if v > 1:
                                print('(G){}*{}(L)={}'.format(len(G_poss), len(L), len(G_poss)*len(L)))
                                n = 0
                        for g in G_poss:                                                                        #Pour chaque "gille" encore possible
                                for l in L:                                                                     #Pour chaque liste possible
                                        G_1 = change(g[0], rangee[1], l)                                        #On change la ligne
                                        all_poss = grille_coherante(G_1, taille_1, g[1])                        #Puis on regarde si c'est cohérent en updatant l'ensemble des possibles
                                        if v > 2:
                                            affiche(G_1)
                                            print(all_poss)
                                        if all_poss:
                                                G += [(G_1, all_poss)]
                return [g[0] for g in G]
        
        
        nLignes = len(Colonnes)
        nColonnes = len(Lignes)

        Lignes_info,sumL = info(Lignes, nLignes)
        Colonnes_info,sumC = info(Colonnes, nColonnes)
        
        if sumL < sumC :
                G = main_branch(Colonnes, nColonnes, nLignes, Lignes_info, change_ligne, grille_coherante_C)
        else :
                G = main_branch(Lignes, nLignes, nColonnes, Colonnes_info, change_colonne, grille_coherante_L)

        
        return G
