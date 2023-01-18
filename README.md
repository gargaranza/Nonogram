# Nonogram
Nonogram solver

# Comment ça marche
Écrire les colonnes puis les lignes comme les exemples données dans la Batterie_de_tests.
Ouvrir le Main et lancer le solve avec la méthode choisie et votre nom de fichier (en .txt).

# Limites
La V1 résoud le 25x25_rand (très simple) en moins d'1 minute et des 20x20 sans trop de problèmes, plus est trop long
La V2 et V2_bis sont très similaires et résolvent les 30x30_simple en 2 minutes
La V4 résoud les 30x30_simple en 30 secondes, mais les 30x30 plus complexes sont trop long et j'ai un MemoryError
La V3 est la pire, elle résoud très rapidement les 15x15 mais à partir du 20x20 j'ai un MemoryError
