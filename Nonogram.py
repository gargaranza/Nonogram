from time import *
from random import *
from Outils import *


def ligne(G, n) : return G[n]

def colone(G, n) :
        if type(G[0]) == int : return [G[n]]
        return [i[n] for i in G]

def change_ligne(G, n, liste) :
        g = [[i for i in j] for j in G]
        g[n] = list(liste)
        return g

def change_colone(G, n, liste) :
        g = [[i for i in j] for j in G]
        for i in range(len(g)) :
                g[i][n] = liste[i]
        return g

def suite_correcte(Cases, i, n) :
	try :
		for j in range(n) :
			if not(Cases[i + j]) :
				return False
	except IndexError : return False
	return True

def liste_coherante(Cases, Lcorrecte) :
        def coherant(L1,L2) :
                for i in range(len(L1)) :
                        if (L1[i], L2[i]) == (0,1) or (L1[i], L2[i]) == (1,0) : return False
                return True

        for i in Lcorrecte :
                if coherant(i,Cases) : return True
        return False
	
	
def grille_coherante_old(G, Lignes, Colones, Lcorrecte, Ccorrecte) :
        for i in range(len(Lignes)) :
                if not(liste_coherante(ligne(G, i), Lcorrecte[i])) :
                        #print('Ligne {} : {}, {}'.format(i, ligne(G, i), Lignes[i]))
                        return False
        for i in range(len(Colones)) :
                if not(liste_coherante(colone(G, i), Ccorrecte[i])) :
                        #print('Colone {} : {}, {}'.format(i, colone(G, i), Colones[i]))
                        return False
        return True

def grille_coherante_L(G, Listes, Lcorrecte) :
        for i in range(len(Listes)) :
                if not(liste_coherante(ligne(G, i), Lcorrecte[i])) :
                        return False
        return True
def grille_coherante_C(G, Listes, Lcorrecte) :
        for i in range(len(Listes)) :
                if not(liste_coherante(colone(G, Listes[i]), Lcorrecte[i])) :
                               return False
        return True

def liste_correcte(Cases, Liste) :
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

def grille_correcte(G, Lignes, Colones) :
        for i in range(len(Lignes)) :
                if not(liste_correcte(ligne(G, i), Lignes[i])) : return False
        for i in range(len(Colones)) :
                if not(liste_correcte(colone(G, i), Colones[i])) : return False
        return True

def create_all_poss(Liste, taille) :
        v = 0
        X = []
        for l in Liste :
                L = [(0,),(1,)]
                for i in range(1,taille) :
                        L_poss = tuple([l for l in L])
                        L = []
                        for k in L_poss :
                                for b in [0,1] :
                                        L_1 = k + (b,)
                                        ajout = True
                                        T_poss = []
                                        c = 0
                                        n0 = 0
                                        for e in L_1 :
                                                if e == 1 :
                                                        c += 1
                                                elif e == 0 :
                                                        if c != 0 :
                                                                T_poss += [c]
                                                                c = 0
                                                        n0 += 1
                                                else :
                                                        break
                                        if c != 0 :
                                                T_poss += [c]
                                        if v : print('i : {}, k : {}, b : {}, L_1 : {}, L : {}, L_poss : {}, T_poss : {}, n0 : {}'.format(i,k,b,L_1,L,L_poss,T_poss,n0))
                                        for p in range(len(T_poss)) :
                                                try :
                                                        if T_poss[p] != l[p] and (p != len(T_poss) - 1 or T_poss[p] > l[p]) :
                                                                ajout = False
                                                                if v : print('non ajouté car T_poss fit pas')
                                                                break
                                                except IndexError :
                                                        if v : print('index error')
                                                        ajout = False
                                        if n0 > taille - sum(l) :
                                                if v : print('non ajouté car trop de 0')
                                                ajout = False
                                        
                                        if ajout :
                                                if v : print('ajouté')
                                                L += [tuple(L_1)]
                
                X += [tuple(L)]
                
        return X
        #return [tuple([j for j in Mots_c_b(taille, 2) if liste_correcte(j,c)]) for c in Liste]
        
        

def affiche(G) :
        if not(G) : return False
        for i in range(len(G)) :
                if i % 5 == 0 :
                        print(' ', end = '')
                        for k in range(2 * (len(G[0]) + len(G[0]) // 5) - 1) :
                                print('-', end = '')
                        print()
                for j in range(len(G[i])) :
                        if j % 5 == 0 : print('|', end = ' ')
                        if G[i][j] == 1 : print('0', end = ' ')
                        elif G[i][j] == 0 : print(' ', end = ' ')
                        else : print('_', end = ' ')
                print('|')
        print(' ', end = '')
        for k in range(2 * (len(G[0]) + len(G[0]) // 5) - 1) :
                print('-', sep = '', end = '')
        print()


def SolveNonogram(Lignes, Colones) :
        #if len(Lignes) == len(Colones) : taille = len(Lignes)
        #else : return False
        L = create_all_poss(Lignes,len(Colones))
        C = create_all_poss(Colones,len(Lignes))
        #I = [0] * len(Colones)
        G_1 = []

        #G_1 = lignes en cours d'étude possible
        for i in L[0] :
                #Tri des colones où il y a un 0
                for j in range(len(Colones)) :
                        if Colones[j] == (0,) and not(i[j]) : break
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
                                P = [tuple([-1 for i in range(len(Colones))]) for j in range(len(Lignes))]
                                #On remplie le début de la Grille
                                for l in range(len(G[k])) :
                                        P[l] = G[k][l]
                                P[len(G[k])] = j

                                #on test si la ligne peut etre ajoutée
                                #print('P : {}\nLignes : {}\nColones : {}\nL : {}\nC : {}\n'.format(P,Lignes,Colones,L,C))
                                if grille_coherante_old(P, Lignes, Colones, L, C) :
                                        #On ajoute la ligne
                                        print(G[k] + [(j)])
                                        G_1 += [G[k] + [(j)]]

        G = []
        for i in G_1 :
                if grille_correcte(i, Lignes, Colones) :
                        G += [i]

        for i in G :
                affiche(i)

def solve_bis(Lignes, Colones) :
        
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
                Ccorrecte = create_all_poss(Colones,len(Lignes))
                for rangee in Lignes_info :
                        print('rangee', rangee)
                        G_poss = G
                        G = []
                        L = create_all_poss((rangee[2],),len(Colones))[0]
                        for g in G_poss :
                                for l in L :
                                        G_1 = change_ligne(g, rangee[1], l)
                                        if grille_coherante_C(G_1, Colones, Ccorrecte) :
                                                G += [G_1]
        else :
                Lcorrecte = create_all_poss(Lignes,len(Colones))
                for rangee in Colones_info :
                        print('rangee', rangee)
                        G_poss = G
                        G = []
                        L = create_all_poss((rangee[2],),len(Lignes))[0]
                        for g in G_poss :
                                for l in L :
                                        G_1 = change_colone(g, rangee[1], l)
                                        if grille_coherante_L(G_1, Lignes, Lcorrecte) :
                                                G += [G_1]
                
        G_1 = []
        for i in G :
                if grille_correcte(i, Lignes, Colones) :
                        G_1 += [i]

        for i in G_1 :
                affiche(i)


        
        
        
def str_to_tuple(S) : return tuple(tuple([int(k) for k in i.split(',')]) for i in S.split('\n') if i != '')

C = """
6,1,2,1,1,1
2,2,4,1,1,9
1,2,7,3,1,1
5,4,1,1,1,6
3,14,3
3,3,2,1,1,7
10,3,1,1,3
1,1,12,1,3,1
3,1,2,4,6,1
2,2,4,5,1,5
2,1,2,4,1,1,3,3
8,1,4,3,1,2
7,5,4,2
1,3,12,1,1
1,7,1,1,7,1
2,1,1,1,1,5,4
1,1,1,1,3,7
2,2,11,2,1
4,14,3
2,4,1,3,3,7
5,2,1,3,1,3,1,2
1,2,1,1,1,2,7
6,1,1,1,2,8
6,2,2,4,1,1
1,5,1,2,1,1,1,1
"""

L ="""
1,5,5,1,7
7,5,1,3,2
1,7,2,2,2,1,3
2,1,1,1,5,9
4,3,1,4,6
1,1,11,3,3
2,1,3,3,1,5,1
4,4,1,2,1,1,1
10,1,1,4
7,5,1,2,3
1,1,1,2,3,3
5,2,4,8
1,1,10,4,2
2,1,4,1,6,1
1,11,4,4
1,1,1,13
1,1,8,3
6,1,5,2,5
2,2,5,11
6,1,1,4,6
1,3,8,2,1,3
3,1,3,1,4,4,1
2,5,2,1,2,2,3
1,4,4,2,5
5,2,3,8,3
"""


D = time()
#SolveNonogram(str_to_tuple(L), str_to_tuple(C))
solve_bis(str_to_tuple(L), str_to_tuple(C))
F = time()
print(sec_to_time(int(F-D)))

"""

D = time()
M = Mots_c_b(5,2)
F = time()
print(sec_to_time(int(F-D)))
for i in M :
        print(i)


"""













