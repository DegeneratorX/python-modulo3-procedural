"""
Para o desempacotamento de dicionários,
utiliza-se .keys(), .values() e .items() também!
"""

d = {'chave1': 'valor1',
     'chave2': 'valor2',
     'chave3': {'nome': 'Victor',
                'idade': 25
                }
     }

k1, k2, k3 = d.keys()  # Desempacotamento apenas de chaves (pode usar sem .keys() também)
print(k1, k2, k3)

v1, v2, v3 = d.values()  # Desempacotando apenas valores
print(v1, v2, v3)

ksub1, ksub2 = d['chave3'].keys()  # Desempacotando o subdicionário especificando a chave onde o subdicionário está.
print(ksub1, ksub2)
# Para fazer desempacotamentos de subsub...subdicionários, é preciso usar outro []. Ex: d[chave1][nome][etc...]

vsub1, vsub2 = d['chave3'].values()  # Desempacotando o subdicionário, pegando apenas os valores ao invés de chaves.
print(vsub1, vsub2)

#######################################
print()

i1, i2, i3 = d.items()  # Desempacotamento de itens do dicionário. Elas viram pares de tuplas.
print(i1, i2, i3, type(i3))

isub1, isub2 = d['chave3'].items()  # Desempacotamento de itens do subdicionário.
print(isub1, isub2)

#######################################
print()
# Desempacotamento usando *

kpacote1, *kpacote2 = d.keys()  # Desempacota o resto automaticamente numa lista usando *.
print(kpacote1, *kpacote2, kpacote2)

ipacote1, *ipacote2 = d.items()
print(ipacote1, *ipacote2, ipacote2)
