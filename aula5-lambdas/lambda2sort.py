"""
Ordenar listas com lambda
.sort() e sorted() normalmente não entendem como ordenar lista dentro de lista.
"""
#  Exemplo: produtos, preços
lista = [
    ['P1', 13],
    ['P3', 7],
    ['P5', 8],
    ['P4', 50],
    ['P2', 6],
]


def func(item):
    return item[1]  # Escolho o índice 1 da lista (de 0 a 1) para ordenar. Ou seja, os preços.


lista.sort(key=func, reverse=True)  # Baseado no que retorna na função, ele ordena. Reverse ordena ao contrário.
print(lista)

#############################################
print("==============")
# O problema disso é que precisa criar uma função só pra ordenar.
# Expressões lambda solucionam o problema.

lista2 = [
    ['P1', 13],
    ['P3', 7],
    ['P5', 8],
    ['P4', 50],
    ['P2', 6],
]

lista2.sort(key=lambda item: item[1], reverse=False)
print(lista2)

#############################################
# Usar .sort() altera a lista pra sempre. Uma solução é usar sorted().
# sorted() passa o valor pra outra variável ou temporariamente se utiliza pra printar.
#############################################
print("=============")

lista3 = [
    ['P1', 13],
    ['P3', 7],
    ['P5', 8],
    ['P4', 50],
    ['P2', 6],
]

print(sorted(lista3, key=lambda i: i[0], reverse=False))  # índice 0 = ordena o produto do menor pro maior.
print(lista3)  # Provando que a lista não foi alterada permanentemente.
