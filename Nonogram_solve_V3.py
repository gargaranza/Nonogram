from Outils import *
from Utilitaires_nonogram import *



def solve(Lignes, Colones, bis=False):

    def info(Liste, taille, l) :
        Liste_info = []
        for i, e in enumerate(Liste) :
            if e == (0,) : p = 1
            else : p = Cnk(taille - sum(e) + 1 - len(e), taille - sum(e) + 1)
            Liste_info += [(p, i, l, e)] #p:possibilities ; i:index ; l:letter ; e:element
        Liste_info = sorted(Liste_info)
        return Liste_info

    v=0
    
    Liste_infos = fusion(info(Lignes, len(Colones), 'L'), info(Colones, len(Lignes), 'C'))
    
    all_poss = (create_all_poss_bis if bis else create_all_poss)
    All_lignes_possible = all_poss(Lignes,len(Colones))
    All_colonnes_possible = all_poss(Colones,len(Lignes))

    G = [[[-1 for i in range(len(Colones))] for j in range(len(Lignes))]]
    for rangee in Liste_infos :
        print('rangee', rangee)
        G_poss = G
        G = []
        Listes_poss = (All_lignes_possible if rangee[2] == 'L' else All_colonnes_possible)
        L = Listes_poss[rangee[1]]
        if v:
            prod = len(G_poss)*len(L)
            print('(G){}*{}(L)={}'.format(len(G_poss), len(L), prod))
            n = 0
        for g in G_poss:
            for l in L:
                if v:
                    n += 1
                    if n%100000 == 0: print('{}({}%)'.format(n, n/prod))
                if coherant((ligne if rangee[2] == 'L' else colone)(g, rangee[1]), l):
                    G += [(change_ligne if rangee[2] == 'L' else change_colone)(g, rangee[1], l)]

    return G

















