from Outils import *


def ligne(G, n): return G[n]

def colone(G, n):
        if type(G[0]) == int : return [G[n]]
        return [i[n] for i in G]


def change_ligne(G, n, liste):
        g = [[i for i in j] for j in G]
        g[n] = list(liste)
        return g

def change_colone(G, n, liste):
        g = [[i for i in j] for j in G]
        for i in range(len(g)) :
                g[i][n] = liste[i]
        return g

    
def suite_correcte(Cases, i, n):
        try:
                for j in range(n):
                        if not(Cases[i + j]):
                                return False
        except IndexError: return False
        return True



def create_all_poss(Liste, taille):
        v = 0
        X = []
        for l in Liste :
                L = [(0,),(1,)]
                for i in range(1,taille):
                        L_poss = tuple([l for l in L])
                        L = []
                        for k in L_poss:
                                for b in [0,1]:
                                        L_1 = k + (b,)
                                        ajout = True
                                        T_poss = []
                                        c = 0
                                        n0 = 0
                                        for e in L_1:
                                                if e == 1:
                                                        c += 1
                                                elif e == 0:
                                                        if c != 0:
                                                                T_poss += [c]
                                                                c = 0
                                                        n0 += 1
                                                else:
                                                        break
                                        if c != 0:
                                                T_poss += [c]
                                        if v: print('i : {}, k : {}, b : {}, L_1 : {}, L : {}, L_poss : {}, T_poss : {}, n0 : {}'.format(i,k,b,L_1,L,L_poss,T_poss,n0))
                                        for p in range(len(T_poss)):
                                                try:
                                                        if T_poss[p] != l[p] and (p != len(T_poss) - 1 or T_poss[p] > l[p]):
                                                                ajout = False
                                                                if v: print('non ajouté car T_poss fit pas')
                                                                break
                                                except IndexError:
                                                        if v: print('index error')
                                                        ajout = False
                                        if n0 > taille - sum(l):
                                                if v: print('non ajouté car trop de 0')
                                                ajout = False
                                        
                                        if ajout:
                                                if v: print('ajouté')
                                                L += [tuple(L_1)]
                
                X += [tuple(L)]
                
        return X

def liste_correcte(l, Liste, taille, strict=False):
        v = 0
        if v: print(l, Liste, taille)
        if v: print("{} '0' (Max: {}), {} '1' (Max: {})".format(l.count(0), taille - sum(Liste), l.count(1), sum(Liste)))
        if strict:
                if len(l) != taille: return False
                if l.count(0) != taille - sum(Liste): return False
                if l.count(1) != sum(Liste): return False
        else:
                if l.count(0) > taille - sum(Liste): return False
                if l.count(1) > sum(Liste): return False
        L = [-1] + list(Liste)
        for b in l:
                if v: print('b', b)
                if b == 0 and L[0] > 0 or b == 1 and L[0] == 0 or b != 0 and b != 1:
                    if v: print('Suite incorrecte, b:{}, L[0]:{}'.format(b, L[0]))
                    return False
                if b == 0 and L[0] == 0 or b == 1 and L[0] > 0:
                    if v: print('Suite bonne, b:{}, L[0]:{}'.format(b, L[0]))
                    L[0] -= 1
                elif b == 1 and L[0] == -1:
                    if v: print('Nouvelle suite, b:{}, L[0]:{}'.format(b, L[0]))
                    L=L[1:]
                    L[0] -= 1
                else:
                    if v: print('Rien, b:{}, L[0]:{}'.format(b, L[0]))
        if v: print('Good')
        return True

def create_all_poss_bis(Liste, taille):
        X = []
        for l in Liste:
                L = Mots_c_b(taille, 2, f_suf = lambda li: liste_correcte(li, l, taille))
                X += [tuple(L)]
                
        return X


def liste_coherante(Cases_fixees, Listes_possibles):
        def coherant(L1,L2):
                for i in range(len(L1)):
                        if (L1[i], L2[i]) == (0,1) or (L1[i], L2[i]) == (1,0): return False
                return True

        for liste in Listes_possibles:
                if coherant(liste, Cases_fixees): return True
        return False



def grille_correcte(G, Lignes, Colones):
        for i, e in enumerate(Lignes):
                if not(liste_correcte(ligne(G, i), e, len(G[0]), True)): return False
        for i, e in enumerate(Colones):
                if not(liste_correcte(colone(G, i), e, len(G), True)): return False
        return True


def affiche(G) :
        if not(G) : return False
        for i in range(len(G)) :
                if i % 5 == 0 :
                        print(' ' + '-' * (2 * (len(G[0]) + len(G[0]) // 5) - 1))
                for j in range(len(G[i])) :
                        if j % 5 == 0 : print('|', end = ' ')
                        if G[i][j] == 1 : print('0', end = ' ')
                        elif G[i][j] == 0 : print(' ', end = ' ')
                        else : print('_', end = ' ')
                print('|')
        print(' ' + '-' * (2 * (len(G[0]) + len(G[0]) // 5) - 1))



