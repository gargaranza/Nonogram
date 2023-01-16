from Outils import *
from Utilitaires_nonogram import *


def grille_coherante_L(G, Listes, Lcorrecte) :
        for i in range(len(Listes)) :
                if not(liste_coherante(ligne(G, i), Lcorrecte[i])) :
                        return False
        return True

def grille_coherante_C(G, Listes, Lcorrecte) :
        for i in range(len(Listes)) :
                if not(liste_coherante(colone(G, i), Lcorrecte[i])) :
                               return False
        return True


def solve(Lignes, Colones) :
        
        def info(Liste, taille) :
                Liste_info = []
                Sum = 0
                for i in range(len(Liste)) :
                        if Liste[i] == (0,) : p = 1
                        else : p = Cnk(taille - sum(Liste[i]) + 1 - len(Liste[i]), taille - sum(Liste[i]) + 1)
                        Liste_info += [(p, i, Liste[i])]
                        Sum += p
                Liste_info = sorted(Liste_info)
                return Liste_info, Sum

        Lignes_info,sumL = info(Lignes, len(Colones))
        Colones_info,sumC = info(Colones, len(Lignes))
        
        G = [[[-1 for i in range(len(Colones))] for j in range(len(Lignes))]]
        if sumL < sumC :
                Ccorrecte = create_all_poss_bis(Colones,len(Lignes))
                for rangee in Lignes_info :
                        print('rangee', rangee)
                        G_poss = G
                        G = []
                        L = create_all_poss_bis((rangee[2],),len(Colones))[0]
                        for g in G_poss :
                                for l in L :
                                        G_1 = change_ligne(g, rangee[1], l)
                                        if grille_coherante_C(G_1, Colones, Ccorrecte) :
                                                G += [G_1]
        else :
                Lcorrecte = create_all_poss_bis(Lignes,len(Colones))
                for rangee in Colones_info :
                        print('rangee', rangee)
                        G_poss = G
                        G = []
                        L = create_all_poss_bis((rangee[2],),len(Lignes))[0]
                        for g in G_poss :
                                for l in L :
                                        G_1 = change_colone(g, rangee[1], l)
                                        if grille_coherante_L(G_1, Lignes, Lcorrecte) :
                                                G += [G_1]
                
        G_1 = []
        for i in G :
                if grille_correcte(i, Lignes, Colones) :
                        G_1 += [i]

        return G_1


