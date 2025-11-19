import sys
import time


def gera():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel


g = gera()

print(next(g))  # Sempre que chamar a função, o objeto é iterado.
print(next(g))  # Ou seja, sempre que eu chamo essa função com .next(), ela me retorna o "próximo" valor.
print(next(g))
# print(next(g) -> se eu colocasse mais um desse, acarretaria em erro de exceção, p
# pois não existe um 4° valor pra iterar.

for v in g:  # Curiosidade:
    print(v)  # Esse for não será executado. Pois 'g' já foi previamente iterado.
