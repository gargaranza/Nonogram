from time import time
from Utilitaires_nonogram import affiche
import Nonogram_solve_V1 as NV1
import Nonogram_solve_V2 as NV2
import Nonogram_solve_V3 as NV3
import Nonogram_solve_V4 as NV4


#Transformation de secondes en temps compréhensible
def sec_to_time(s):
        if s < 60: return '{:>2} s'.format(s)
        elif s < 3600: return '{:>2} min {:>2} s'.format(s//60,s%60)
        elif s < 86400: return '{:>2} h {:>2} min {:>2} s'.format(s//3600,s%3600//60,s%60)
        elif s < 31536000: return '{:>3} j {:>2} h {:>2} min {:>2} s'.format(s//86400,s%86400//3600,s%3600//60,s%60)
        else: return '{:>4} ans {:>3} j {:>2} h {:>2} min {:>2} s'.format(s//31536000,s%31536000//86400,s%86400//3600,s%3600//60,s%60)


#Transformation des données brut en tuples
def str_to_tuple(S) : return tuple(tuple([int(k) for k in i.split(',')]) for i in S.split('\n') if i != '')

#Extraction des Lignes et Colonnes à partir du nom du fichier
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
        case 'V4':
            return NV4.solve
        case _:
            print('Method not found')
    

#Comparaison du temps de différentes méthodes
def test_speed_2(method_1, method_2, file):
    (C, L) = file_to_list(file)
    
    print('method 1')
    D = time()
    switch_method(method_1)(L, C)
    M1 = time()
    print('method 2')
    M2 = time()
    switch_method(method_2)(L, C)
    F = time()
        
    print('time {}: {}\ntime {}: {}'.format(method_1, sec_to_time(int(M1-D)), method_2, sec_to_time(int(F-M2))))

def test_speed_3(method_1, method_2, method_3, file):
    (C, L) = file_to_list(file)
    
    print('method 1')
    D = time()
    switch_method(method_1)(L, C)
    M1 = time()
    print('method 2')
    M2 = time()
    switch_method(method_2)(L, C)
    M3 = time()
    print('method 3')
    M4 = time()
    switch_method(method_3)(L, C)
    F = time()
        
    print('time {}: {}\ntime {}: {}\ntime {}: {}'.format(method_1, sec_to_time(int(M1-D)),
                                                         method_2, sec_to_time(int(M3-M2)),
                                                         method_3, sec_to_time(int(F-M4))))

#Résoud le nonogram avec la méthode choisie à partir du fichier
def solve(method, file):
    (C, L) = file_to_list(file)

    D = time()
    Grilles = switch_method(method)(L, C)
    F = time()

    for g in Grilles:
        affiche(g)
    print('time: {}'.format(sec_to_time(int(F-D))))


if __name__ == '__main__':
    solve('V3', '15x15_test')
    #test_speed_2('V1', 'V2', '25x25_rand')
    #test_speed_3('V2', 'V2_bis', 'V4', '30x30_simple_2')
    




