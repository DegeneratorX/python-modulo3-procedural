"""
Adições e remoções usando .pop(), .popitem() e .update()
"""

d1 = {
    1: 2,
    2: 3,
    4: 5
}  # k: v

print(d1)

d1.pop(2)  # Dá um pop na chave 2. Ou seja, elimina.
print(d1)

d1.popitem()  # Elimina o último item no dicionário. No caso será agora a chave 4.
print(d1)

d2 = {
    'a': 'b',
    'c': 'd'
}
d1.update(d2)  # Concatena os dois dicionários.
print(d1)
