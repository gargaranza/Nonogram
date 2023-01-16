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
        nLignes = len(Colones)
        nColones = len(Lignes)
        
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

        Lignes_info,sumL = info(Lignes, nLignes)
        Colones_info,sumC = info(Colones, nColones)
        
        G = [[[-1 for i in range(nLignes)] for j in range(nColones)]]
        if sumL < sumC :
                All_colonnes_possible = create_all_poss(Colones,nColones)
                for rangee in Lignes_info :
                        print('rangee', rangee)
                        G_poss = G
                        G = []
                        L = create_all_poss((rangee[2],),nLignes)[0]
                        for g in G_poss :
                                for l in L :
                                        G_1 = change_ligne(g, rangee[1], l)
                                        if grille_coherante_C(G_1, nColones, All_colonnes_possible):
                                                G += [G_1]
        else :
                All_lignes_possible = create_all_poss(Lignes,nLignes)
                for rangee in Colones_info:
                        print('rangee', rangee)
                        G_poss = G
                        G = []
                        L = create_all_poss((rangee[2],),nColones)[0]
                        for g in G_poss :
                                for l in L :
                                        G_1 = change_colone(g, rangee[1], l)
                                        if grille_coherante_L(G_1, nLignes, All_lignes_possible) :
                                                G += [G_1]
                
        G_1 = []
        for i in G :
                if grille_correcte(i, Lignes, Colones) :
                        G_1 += [i]

        return G_1


