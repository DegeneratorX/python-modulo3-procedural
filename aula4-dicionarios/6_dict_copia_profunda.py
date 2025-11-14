"""
deepcopy() - cria uma cópia profunda da lista.

deep copy (cópia profunda) não é necessária para dicionários não-aninhados, mas 
é importante quando o dicionário contém outras listas ou dicionários ou objetos mutáveis.

Altamente custoso, pois cria uma nova estrutura de dados na memória, copiando todos os elementos recursivamente
(inclusive os elementos internos). Complexidade O(n*m), onde n é o número de elementos no dicionário
e m é o número de elementos dentro dos elementos (no caso de listas ou dicionários internos).

Para copiar realmente um dicionário pra uma variável de forma profunda,
é preciso usar o módulo 'copy', importando.
Ou seja, é o melhor método possível para cópia de valores.
Usando copy.deepcopy(x).
"""

import copy

d1 =    {
            'chave1': 'a', 
            'chave2': 'b', 3: 'c', 
            'chave_lista': ['trynda', 'mere']
        }
v = copy.deepcopy(d1)  # Pronto, as duas variáveis são totalmente independentes.

v['chave1'] = 'Victor'
v['chave_lista'] = 'Joao'

print("Dicionário d1:", d1)
print("Dicionário v:", v)
print("Comparando d1 == v:", d1 == v)  # Agora são realmente separados. Aqui resulta em False.