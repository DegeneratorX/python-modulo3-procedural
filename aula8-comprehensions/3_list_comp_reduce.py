"""
Reduce

Em list comprehensions, o reduce não é tão comum quanto map e filter, mas pode 
ser implementado usando a função `functools.reduce` em conjunto com uma list 
comprehension para preparar os dados.
"""

from functools import reduce

# Lista de números de 0 a 9
lista = list(range(10))

# Usando list comprehension para criar uma nova lista com os quadrados dos números
quadrados = [x ** 2 for x in lista]
print("Lista de quadrados:", quadrados)

# Usando reduce para somar todos os quadrados
soma_dos_quadrados = reduce(lambda x, y: x + y, quadrados)
print("Soma dos quadrados:", soma_dos_quadrados)





print("\n#############################################\n")
"""
Reduce com filtro em list comprehension
"""

# Usando list comprehension para criar uma nova lista com os quadrados dos números pares
quadrados_pares = [x ** 2 for x in lista if x % 2 == 0]
print("Lista de quadrados dos números pares:", quadrados_pares)
# Usando reduce para somar todos os quadrados dos números pares
soma_dos_quadrados_pares = reduce(lambda x, y: x + y, quadrados_pares)
print("Soma dos quadrados dos números pares:", soma_dos_quadrados_pares)