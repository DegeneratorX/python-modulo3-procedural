"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(cidades, estados)  # zip() cria um iterador...
print(cidades_estados, type(cidades_estados))  # (Tipo 'zip'.)
print(next(cidades_estados))  # ...portanto é possível iterar sobre ele usando next.

for valor in cidades_estados:
    print(valor)  # Printando o restante.

# O zip() une iteráveis e faz uma espécie de pares em tuplas. O que sobrar não é contabilizado (Monte Belo).
# Para incluir os que sobraram e fazer pares com 'None', usa-se zip_longest().

#############################################
print('#' * 30)

