"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem Importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""

from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

for grupo in combinations(pessoas, 2):  # Combinação de 10 2 a 2
    print(grupo)  # Tuplas com pares de 2 com todas as combinações possíveis, onde a ordem não importa.

print('#'*20)

for grupo in permutations(pessoas, 2):  # Permutação de 10 2 a 2
    print(grupo)  # Tuplas com pares de 2 com todas as permutações possíveis, onde a ordem importa.

print('#'*20)

for grupo in product(pessoas, repeat=2):  # Produto de 10 2 a 2
    print(grupo)  # Tuplas com pares de 2 com todos os produtos possíveis, repetindo também os mesmos valores, por ex:
#                   ('Luiz', 'Luiz')
