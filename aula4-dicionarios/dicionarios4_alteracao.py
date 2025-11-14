"""
Alteração de valores no dicionário
"""

d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla'
}

print(d1)

d1['str'] = 'Alterei o valor de str'  # Alteração de um valor existente. Bem parecido com listas.
print(d1['str'])

# Outra forma de alterar é usando .update(), segue o código:

d1.update({'nova_chave':'novo_valor'})  # Tbm posso colocar novos valores com .update().
d1.update({123: 911})

print(d1)

#############################################
print()

# Apagar valores: utiliza-se 'del'.

del d1['str']
print(d1)
