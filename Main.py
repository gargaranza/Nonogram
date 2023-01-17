from time import time
from Outils import sec_to_time
from Utilitaires_nonogram import affiche
import Nonogram_solve_V1 as NV1
import Nonogram_solve_V2 as NV2
import Nonogram_solve_V3 as NV3


def str_to_tuple(S) : return tuple(tuple([int(k) for k in i.split(',')]) for i in S.split('\n') if i != '')

def file_to_list(name):
    file = open('./Batterie_de_tests/{}.txt'.format(name), 'r')
    tmp = file.read().split('\n\n')
    C = str_to_tuple(tmp[0])
    L = str_to_tuple(tmp[1])
    return C, L

def switch_method(method):
    match method:
        case 'V1':
            return NV1.solve
        case 'V2':
            return NV2.solve
        case 'V2_bis':
            return (lambda C, L: NV2.solve(C, L, True))
        case 'V3':
            return NV3.solve
        case _:
            print('Method not found')
    

def test_speed(method_1, method_2, file):
    (C, L) = file_to_list(file)
    
    D = time()
    switch_method(method_1)(L, C)
    M = time()
    switch_method(method_2)(L, C)
    F = time()
        
    print('time v2: {}\ntime v2_bis: {}'.format(sec_to_time(int(M-D)), sec_to_time(int(F-M))))


def solve(method, file):
    (C, L) = file_to_list(file)

    D = time()
    Grille = switch_method(method)(L, C)
    F = time()
    
    affiche(Grille)
    print('time: {}'.format(sec_to_time(int(F-D)))

if __name__ == '__main__':
    solve('V2_bis', '30x30_Deer')
    
    



