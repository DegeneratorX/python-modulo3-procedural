"""
Para copiar realmente um dicionário pra uma variável de forma profunda,
é preciso usar o módulo 'copy', importando.
Ou seja, é o melhor método possível para cópia de valores.
Usando copy.deepcopy(x).
"""

import copy

d1 = {'chave1': 'a', 'chave2': 'b', 3: 'c', 'chave_lista': ['trynda', 'mere']}
v = copy.deepcopy(d1)  # Pronto, as duas variáveis são totalmente independentes.

v['chave1'] = 'Victor'
v['chave_lista'] = 'Joao'

print(d1)
print(v)
print(d1 == v)  # Agora são realmente separados. Aqui resulta em False.
