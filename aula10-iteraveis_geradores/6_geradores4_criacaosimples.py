"""
Existe uma forma simples de criar gerador a partir de list comprehension.
Trocando os [] por () (NÃO É TUPLA!)
"""

import sys

l1 = [x for x in range(10000)]
l2 = (x for x in range(10000))

print(type(l1), sys.getsizeof(l1), 'bytes')  # Tipo Lista. Consumo excessivo de memória (~80KB)
print(type(l2), sys.getsizeof(l2), 'bytes')  # Class Generator (tipo gerador). Consumo baixo de memória. (~100B)
print()

print(next(l2))  # 0
print(next(l2))  # 1
print(next(l2))  # 2

for v in l2:  # Curiosidade: devido aos 3 'prints' acima, no 'for' será exibido 9997 valores. Começará a partir do 3.
    print(v)  # Isso ocorre pq 3 valores já foram iterados. Ou seja, já se "consumiu" 3 valores do iterador l2.
