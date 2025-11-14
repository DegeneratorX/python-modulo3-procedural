"""
Conversão de dicionario pra tupla ou lista e vice versa.
dict()
"""

lista_ou_tupla = (
    ['c1', 1],
    ('c2', 2),
    ['c3', 3]
)

d1 = dict(lista_ou_tupla)
print(d1)

# Desde que seja formado por pares, é possível converter tuplas ou listas em
# dicionários tranquilamente. Tanto faz se é tuplas e listas misturadas.
