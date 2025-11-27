"""
Dictionary e Set Comprehensions

Posso usar comprehensions para criar dicionários e sets também.
"""

"""
Criando dicionários com dictionary comprehension
"""

lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2')
]

# Mapeando dicionário a partir de uma lista contendo pares de tuplas.
# Para dictionary comprehension, usa-se x: y entre chaves
d1 = {x: y for x, y in lista}

print("d1 criada:", d1)






print("\n#############################################\n")
"""
Criando sets com set comprehension
"""

# Já no caso de criação de set comprehension, usa-se x apenas.
# Criando set, também entre chaves, mas sem x: y, e sim apenas x.
s1 = {x for x, y in lista} 
print("s1 criada:", s1)