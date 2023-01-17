from Outils import *
from Utilitaires_nonogram import *


def grille_coherante_L(G, nLignes, All_lignes_possible):
        for i in range(nLignes):
                if not(liste_coherante(ligne(G, i), All_lignes_possible[i])):
                        return False
        return True

def grille_coherante_C(G, nColonnes, All_colonnes_possible):
        for i in range(nColonnes):
                if not(liste_coherante(colone(G, i), All_colonnes_possible[i])):
                        return False
        return True


def solve(Lignes, Colones):

        def info(Liste, taille):
                Liste_info = []
                Sum = 0
                for i, e in enumerate(Liste) :
                        if e == (0,) : p = 1
                        else : p = Cnk(taille - sum(e) + 1 - len(e), taille - sum(e) + 1)
                        Liste_info += [(p, i, e)]
                        Sum += p
                Liste_info = sorted(Liste_info)
                return Liste_info, Sum

        def main_branch(Liste, taille_1, taille_2, Liste_infos, fonction):
                All_listes_possible = create_all_poss_bis(Liste,taille_1)
                for rangee in Lignes_info :
                        print('rangee', rangee)
                        G_poss = G
                        G = []
                        L = create_all_poss_bis((rangee[2],),taille_2)[0]
                        if v:
                                print('(G){}*{}(L)={}'.format(len(G_poss), len(L), len(G_poss)*len(L)))
                                n = 0
                        for g in G_poss :
                                for l in L :
                                        if v:
                                                n += 1
                                                if n%1000 == 0: print(n) 
                                        G_1 = change_ligne(g, rangee[1], l)
                                        if fonction(G_1, taille_1, All_listes_possible):
                                                G += [G_1]
        
        v = 1
        
        nLignes = len(Colones)
        nColones = len(Lignes)

        Lignes_info,sumL = info(Lignes, nLignes)
        Colones_info,sumC = info(Colones, nColones)
        
        G = [[[-1 for i in range(len(Colones))] for j in range(len(Lignes))]]
        if sumL < sumC :
                main_branch(Colonnes, nColones, nLignes, grille_coherante_C)
        else :
                main_branch(Lignes, nLignes, nColones, grille_coherante_L)
                
        G_1 = []
        for i in G :
                if grille_correcte(i, Lignes, Colones) :
                        G_1 += [i]

        return G_1


