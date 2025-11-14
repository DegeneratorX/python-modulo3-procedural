"""
Alteração de valores no dicionário

Utiliza-se o nome do dicionário, colchetes e a chave existente para alterar o valor.
Também pode-se usar o método .update() para alterar valores. A diferença é que com 
.update() pode-se alterar vários valores de uma vez só.
"""

d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla'
}

# Inserindo um novo par chave-valor. Insere no último lugar.
d1['nova_chave'] = 'novo_valor'

# Alteração de um valor existente. Bem parecido com listas.
d1['str'] = 'Alterei o valor de str'
print("Novo valor de d1['str']:", d1['str'])

# Outra forma de alterar é usando .update(), segue o código:
# Tbm posso colocar novos valores com .update().
d1.update({'nova_chave': 'novo_valor'})
d1.update({123: 911})

print("d6 atualizado: ", d1)

print("\n############################################\n")

"""
Concatenação de dicionários

- Para concatenar dicionários, pode-se usar o método .update() ou o operador ** (desempacotamento).
- Com o .update(), o dicionário original é modificado.
- Com o operador ** é criado um novo dicionário.
"""

d2 = {
    'chave1': 'valor1',
    'chave2': 'valor2'
}

d3 = {
    'chave3': 'valor3',
    'chave4': 'valor4'
}

# Usando .update() - modifica o dicionário original
d2.update(d3)
print("Dicionário d2 após update com d3:", d2)
# Usando ** (conceito será abordado depois) - cria um novo dicionário (kwargs)

d4 = {**d2, **d3}
print("Novo dicionário d4 com desempacotamento de d2 e d3:", d4)

print("\n############################################\n")

"""
Apagar elementos de um dicionário

- Utiliza-se 'del' para apagar elementos de um dicionário.
- Usa-se o método .pop() para apagar um elemento específico, ou popitem() para 
apagar o último elemento adicionado e retorná-lo.
- Também pode-se usar o método .clear() para apagar todos os elementos do dicionário.
"""

d5 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla',
    'nova_chave': 'novo_valor',
    "chave_extra": "valor extra"
}

# Apagar valores: utiliza-se 'del'.
del d5['str']
print("Dicionário após apagar 'str' com del:", d5)

# Apagar valores: utilizando .pop()
valor_removido = d5.pop(123)  # Remove o item com chave
print("Valor removido com pop():", valor_removido)
print("Dicionário após usar pop() para remover chave 123:", d5)

# Apagar o último item adicionado: utilizando .popitem()
chave, valor = d5.popitem()  # Remove o último item adicionado
print(f"Último item removido com popitem(): chave={chave}, valor={valor}")
print("Dicionário após usar popitem():", d5)

# Apagar todos os itens: utilizando .clear()
d5.clear()
print("Dicionário após usar clear():", d5)

print("\n############################################\n")
