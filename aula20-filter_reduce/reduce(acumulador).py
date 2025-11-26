"""
Parâmetros semelhantes ao map() e filter().
reduce() é uma alternativa para acumular valores.
"""

from dados import produtos, pessoas, lista
from functools import reduce
####################
acumula = 0

for valor in lista:
    acumula += valor

print(acumula)  # Acumulador tradicional clássico

#####################
print()
print('#'*40)
print()

# reduce() recebe uma função, um iterável que essa função atuará sobre cada valor, e o valor inicial do acumulador (0).
soma_lista = reduce(lambda acumulador, item: acumulador + item, lista, 0)
print(soma_lista)

#####################
print()
print('#'*40)
print()

soma_precos = reduce(lambda acumulador, produto: round(produto['preco'] + acumulador), produtos, 0)
print(soma_precos)  # Somo todos os preços do meu primiero dicionário
print('Média dos preços:', soma_precos / len(produtos))  # Média de preços

#####################
print()
print('#'*40)
print()

soma_idades = reduce(lambda acumulador, p: acumulador + p['idade'], pessoas, 0)
print('Média das idades:', soma_idades / len(pessoas))  # Média de idade do segundo dicionário.
