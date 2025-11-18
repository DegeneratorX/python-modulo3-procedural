lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2')
]

d1 = {x: y for x, y in lista}  # Criando dicionário a partir de uma lista contendo pares de tuplas.
# Para dictionary comprehension, usa-se x: y entre chaves

# Já no caso de criação de set comprehension, usa-se x apenas.

s1 = {x for x, y in lista}  # Criando set, também entre chaves, mas sem x: y, e sim apenas x.
