"""
Checagem de valores no dicionário utilizando .keys() e .values()
"""

d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla'
}

# Checagem se determinada CHAVE existe no dicionário
print('str' in d1.keys())  # True, pois 'str' é uma chave do dicionário.
print('garrafa' in d1.keys())  # False, pois 'garrafa' não é uma chave do dicionário.

# ALTERNATIVA: Checagem direta (sem usar .keys())
print('str' in d1)
print('garrafa' in d1)


# Checagem se determinado VALOR existe no dicionário
print('valor' in d1.values())  # True, pois 'valor' é um valor do dicionário
print('água' in d1.values())  # False, pois 'água' não é um valor do dicionário.

# Tamanho do dicionário
print(len(d1))  # Mostra a quantidade de pares de chaves e valores juntos. São 3.

print("\n############################################\n")
"""
Iterando com for utilizando .keys(), .values() e .items()
"""

d2 = {
    'chave1': 'valor',
    'chave2': 'outro valor',
    'chave3': 'mais outro valor'
}

for k in d2:  # Mostra apenas as chaves. Pode adicionar d1.keys() também, mas por padrão não precisa colocar.
    print("Chaves de d2: ", k)

print("\n############################################\n")

for v in d2.values():  # Mostra os valores nos dicionários.
    print("Valores de d2: ", v)

print("\n############################################\n")

for i in d2.items():  # Mostra os pares (tupla). Ou seja, os dois, chave e valor. Ao iterar, i vira uma tupla.
    print("Chaves e valores de d2:", i)


print("\n############################################\n")

# Existe outra forma de fazer isso sem aparecer parênteses. Segue abaixo.
for i in d2.items():  # Forma sem parênteses e vírgulas
    print("Chaves e valores de d2:", i[0], i[1])  # Acessando os índices, lembrando que i vira uma tupla ao iterar sobre um dicionário.

print("\n############################################\n")

# Desempacotamento de um dicionário. O método mais utilizado.
for k, v in d2.items():  # Desempacotando, mostra também sem parênteses e sem vírgulas.
    print("Chaves e valores de d2, desempacotados:", k, v)
