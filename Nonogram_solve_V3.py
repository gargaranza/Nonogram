from Utilitaires_nonogram import *

#Fusion de 2 listes triées en gardant l'ordre (tri fusion)
def fusion(L1, L2):
	L = []
	for i in range (len(L1) + len(L2)):
		if L1 == []:
			return L + L2
		elif L2 == []:
			return L + L1
		elif L1[0] <= L2[0]:
			L += [L1[0]]
			L1.pop(0)
		else: 
			L += [L2[0]]
			L2.pop(0)
	return L
    

#Comme le V2 mais on traite indifféremment les lignes et colonnes
def solve(Lignes, Colonnes, v=0):

    #fonction qui calcule le nombre de possibilitées pour chaque contraintes et qui retourne ce nombre (p), l'indice de la colonne/liste (i), la lettre (l) et la liste elle-même (e)
    def info(Liste, taille, l) :
        Liste_info = []
        for i, e in enumerate(Liste) :
            if e == (0,) : p = 1
            else : p = Cnk(taille - sum(e) + 1 - len(e), taille - sum(e) + 1)
            Liste_info += [(p, i, l, e)]
        Liste_info = sorted(Liste_info)
        return Liste_info


    Liste_infos = fusion(info(Lignes, len(Colonnes), 'L'), info(Colonnes, len(Lignes), 'C'))                    #Fusion des infos des colonnes et lignes
    
    All_lignes_possible = create_all_poss_bis(Lignes,len(Colonnes))
    All_colonnes_possible = create_all_poss_bis(Colonnes,len(Lignes))

    G = [[[-1 for i in range(len(Colonnes))] for j in range(len(Lignes))]]                                      #Grille vide
    for rangee in Liste_infos :
        if v: print('rangee', rangee)
        G_poss = G
        G = []
        Listes_poss = (All_lignes_possible if rangee[2] == 'L' else All_colonnes_possible)                      #Switch lignes/colonnes
        L = Listes_poss[rangee[1]]
        if v > 1:
            prod = len(G_poss)*len(L)
            print('(G){}*{}(L)={}'.format(len(G_poss), len(L), prod))
            n = 0
        for g in G_poss:                                                                                        #Pour chaque gille encore possible
            for l in L:                                                                                         #Pour chaque liste possible
                if v > 1:
                    n += 1
                    if n%100000 == 0: print('{}({}%)'.format(n, n/prod))
                if coherant((ligne if rangee[2] == 'L' else colonne)(g, rangee[1]), l):                         #Si on peut changer la ligne/colonne
                    G += [(change_ligne if rangee[2] == 'L' else change_colonne)(g, rangee[1], l)]              #On change et l'ajoute aux possibles

    return G



