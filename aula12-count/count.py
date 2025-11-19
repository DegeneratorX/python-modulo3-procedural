"""
count - Itertools (iteration tools)

Count é iterador, ou seja, dá pra usar a função next().
Diferente da função Range, que é um iterável, não iterador.
"""
from itertools import count

contador = count()

print(next(contador))
print(next(contador))
print(next(contador))
# ...

# EVITE USAR 'FOR' com count()! Pois pode não só travar o programa, como a IDE e consumir memória!
# Usarei tomando precaução.

for valor in contador:
    print(valor)

    if valor >= 10:
        break  # Isso garante que se o valor for maior ou igual a 10, sai do laço e quebra o loop infinito.

######################################
print()

contador2 = count(start=5, step=2)  # step=0.1 também funciona, no caso vai pular de forma decimal.
# start = 5 irá começar no 5.
# step=-1 também funciona, irá contar para trás.
for valor in contador2:
    print(valor)
    if valor >= 10:
        break


