
def fact(N):
	F = 1
	for i in range(2, N + 1):
		F = F * i
	return F

def Cnk(k,n): return fact(n) // (fact(k) * fact(n-k))


def ligne(G, n):
        if type(G[0]) == int : return G
        return G[n]

def colonne(G, n):
        if type(G[0]) == int : return [G[n]]
        return [i[n] for i in G]


def change_ligne(G, n, liste):
        g = [[i for i in j] for j in G]                         #Copie de la grille
        g[n] = list(liste)
        return g

def change_colonne(G, n, liste):
        g = [[i for i in j] for j in G]                         #Copie de la grille
        for i in range(len(g)) :
                g[i][n] = liste[i]
        return g

    
def suite_correcte(Cases, i, n):
        try:
                for j in range(n):                              #Chaque case pour une longueur de n
                        if not(Cases[i + j]):                   #On vérifie si i + j est un 1
                                return False
        except IndexError: return False                         #Si on atteint le bout de la liste
        return True



#Créé l'ensemble des possibilitées respectant les contraintes de Liste
def create_all_poss(Liste, taille, v=0):
        X = []
        for l in Liste :
                L = [(0,),(1,)]                                                                                                         #Liste initiale des possibilitées
                for i in range(1,taille):
                        L_poss = tuple([l for l in L])                                                                                  #Copie de L dans L_poss
                        L = []
                        for k in L_poss:                                                                                                #Pour chaque liste possible
                                for b in [0,1]:
                                        L_1 = k + (b,)                                                                                  #Liste ralongée de b
                                        ajout = True                                                                                    #ajout initialement à True
                                        T_poss = []                                                                                     #Tuple en train d'être créé
                                        c = 0                                                                                           #Longueur de la séquence
                                        n0 = 0                                                                                          #nombre de 0
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
                                        if c != 0:                                                                                      #Pour finir, on rajoute c si non nul
                                                T_poss += [c]
                                        if v: print('i : {}, k : {}, b : {}, L_1 : {}, L : {}, L_poss : {}, T_poss : {}, n0 : {}'.format(i,k,b,L_1,L,L_poss,T_poss,n0))
                                        for p in range(len(T_poss)):
                                                try:
                                                        if T_poss[p] != l[p] and (p != len(T_poss) - 1 or T_poss[p] > l[p]):            #Si la séquence n'est pas de la bonne taille ET que (c'est pas la derniere OU elle est trop longue) 
                                                                ajout = False
                                                                if v: print('non ajouté car T_poss fit pas')
                                                                break
                                                except IndexError:                                                                      #T_poss est composé de trop de séquence (error l[p])
                                                        if v: print('index error')
                                                        ajout = False
                                        if n0 > taille - sum(l):                                                                        #S'il y a trop de 0
                                                if v: print('non ajouté car trop de 0')
                                                ajout = False
                                        
                                        if ajout:                                                                                       #Si tout est bon
                                                if v: print('ajouté')
                                                L += [tuple(L_1)]
                
                X += [tuple(L)]
                
        return X

#Check si la liste est correcte (strict) ou si elle commence de façon correcte
def liste_correcte(l, Liste, taille, strict=False, v=0):
        if v: print(l, Liste, taille)
        if v: print("{} '0' (Max: {}), {} '1' (Max: {})".format(l.count(0), taille - sum(Liste), l.count(1), sum(Liste)))
        if strict:
                if len(l) != taille: return False                                               #Si la liste n'est pas de la bonne taille
                if l.count(0) != taille - sum(Liste): return False                              #S'il n'y a pas le bon nombre de 0
                if l.count(1) != sum(Liste): return False                                       #S'il n'y a pas le bon nombre de 1
        else:
                if l.count(0) > taille - sum(Liste): return False                               #S'il y a trop de 0
                if l.count(1) > sum(Liste): return False                                        #S'il y a trop de 1
                
        L = [-1] + list(Liste)                                                                  #On commence la liste avec un '-1' pour indiquer qu'aucune séquence n'est encore en cours
        for b in l:
                if v: print('b', b)
                if b == 0 and L[0] > 0 or b == 1 and L[0] == 0 or b != 0 and b != 1:            #Si on a un 0 alors qu'on n'a pas fini la séquence OU qu'on &a un 1 alors qu'elle l'est OU que b n'est ni 0 ni 1
                    if v: print('Suite incorrecte, b:{}, L[0]:{}'.format(b, L[0]))
                    return False
                if b == 0 and L[0] == 0 or b == 1 and L[0] > 0:                                 #Si on a un 0 est la séquence vien de finir (donc 0 forcé) ou on a un 1 et la séquence est pas finie
                    if v: print('Suite bonne, b:{}, L[0]:{}'.format(b, L[0]))
                    L[0] -= 1                                                                   #On enlève 1 à la contrainte
                elif b == 1 and L[0] == -1:                                                     #Si on a un 1 et que la contrainte est lachée (L[0]==-1)
                    if v: print('Nouvelle suite, b:{}, L[0]:{}'.format(b, L[0]))
                    L=L[1:]                                                                     #On passe à une nouvelle séquence
                    L[0] -= 1                                                                   #Et on oublie pas d'enlever le 1 à la séquence
                else:
                    if v: print('Rien, b:{}, L[0]:{}'.format(b, L[0]))
        if v: print('Good')
        return True


#Créé l'ensemble des mots de c chiffres en base b respectant les conditions necessaires (f_nec) et suffisantes (f_suf)
def Mots_c_b(c, b, f_nec = lambda l: True, f_suf = lambda l: True):
        L1 = []

        for j in range(b) :
                L1 += [(j,)]

        for n in range(c - 1):
                L = [i for i in L1]
                L1 = []
                for l in L:
                        for j in range(b):
                                e = (l) + (j,)
                                if f_suf(e):
                                        L1 += [e]
        L = [e for e in L1 if f_nec(e)]
        return L


#Créé l'ensemble des possibilitées respectant les contraintes de Liste
def create_all_poss_bis(Liste, taille):
        X = []
        for l in Liste:                                                                         #Pour chaque tuple de contrainte
                L = Mots_c_b(taille, 2, f_suf = lambda li: liste_correcte(li, l, taille))       #On créé toutes les listes binaires de taille "taille" qui respectent la contrainte non stricte de "liste_correcte"
                X += [tuple(L)]
                
        return X

#Deux listes sont cohérentes s'il n'y a pas d'opposition 1-0 (-1 signifie pas de contrainte et donc pas d'obstacle à la cohérence)
def coherant(L1,L2):
                for l1, l2 in zip(L1, L2):
                        if (l1, l2) == (0,1) or (l1, l2) == (1,0): return False
                return True

#Les cases sont cohérentes s'il existe une liste cohérente parmis les listes possibles 
def liste_coherante(Cases_fixees, Listes_possibles):
        for liste in Listes_possibles:
                if coherant(liste, Cases_fixees): return True
        return False


#L'affichage d'une grille
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



