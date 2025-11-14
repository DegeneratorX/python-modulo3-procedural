"""
Checagem de valores no dicionário utilizando .keys() e .values()
"""

d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla'
}


print('str' in d1.keys())  # True, pois 'str' é uma chave do dicionário.
print('garrafa' in d1.keys())  # False, pois 'garrafa' não é uma chave do dicionário.

print('valor' in d1.values())  # True, pois 'valor' é um valor do dicionário
print('água' in d1.values())  # False, pois 'água' não é um valor do dicionário.

print(len(d1))  # Mostra a quantidade de pares de chaves e valores juntos. São 3.

# OBSERVAÇÃO!!!!!!!!!
# print('str' in d1) é equivalente a print('str' in d1.keys()). Por convenção não é necessário adicionar .keys().
