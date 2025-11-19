"""
Importância dos geradores: economia de memória.
Nós não precisamos de todos os valores ao mesmo tempo.
E isso o gerador soluciona.
"""

import sys

lista = list(range(10))

print(sys.getsizeof(lista))  # getsizeof(obj) retorna o número de bytes que o obj consome da memória.

lista2 = list(range(1000))  # Usando lista maior. Maior o consumo de memória.

print(sys.getsizeof(lista2))

