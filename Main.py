from time import time
from Outils import sec_to_time
from Utilitaires_nonogram import affiche
import Nonogram_solve_V1 as NV1
import Nonogram_solve_V2 as NV2
import Nonogram_solve_V2_bis as NV2_bis


def str_to_tuple(S) : return tuple(tuple([int(k) for k in i.split(',')]) for i in S.split('\n') if i != '')

def file_to_list(name):
    file = open('./Batterie_de_tests/{}.txt'.format(name), 'r')
    tmp = file.read().split('\n\n')
    C = str_to_tuple(tmp[0])
    L = str_to_tuple(tmp[1])
    return C, L

def test(C, L):
    D = time()
    Grilles_1 = NV2.solve(L, C)
    M = time()
    Grilles_2 = NV2_bis.solve(L, C)
    F = time()

    for g in Grilles_1:
        affiche(g)
    for g in Grilles_2:
        affiche(g)
        
    print('time v2: {}\ntime v2_bis: {}'.format(sec_to_time(int(M-D)), sec_to_time(int(F-M))))


if __name__ == '__main__':
    
    (C, L) = file_to_list('30x30_simple_2')
    test(C, L)
    
    



