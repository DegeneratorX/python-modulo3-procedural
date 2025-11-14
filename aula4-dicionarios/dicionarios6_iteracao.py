"""
Iterando com for utilizando .keys(), .values() e .items()
"""

d1 = {
    'chave1': 'valor',
    'chave2': 'outro valor',
    'chave3': 'mais outro valor'
}

for k in d1:  # Mostra apenas as chaves. Pode adicionar d1.keys() também, mas por padrão não precisa colocar.
    print(k)

########################################################
print()

for v in d1.values():  # Mostra os valores nos dicionários.
    print(v)

########################################################
print()

for i in d1.items():  # Mostra os pares. Ou seja, os dois, chave e valor. Ao iterar, i vira uma tupla.
    print(i)

# Existe outra forma de fazer isso sem aparecer parênteses. Segue abaixo.

##########################################################
print()

for i in d1.items():  # Forma sem parênteses e vírgulas
    print(i[0], i[1])  # Acessando os índices, lembrando que i vira uma tupla ao iterar sobre um dicionário.

##########################################################
print()
# Desempacotamento de um dicionário. IMPORTANTE!
for k, v in d1.items():  # Desempacotando, mostra também sem parênteses e sem vírgulas.
    print(k, v)
