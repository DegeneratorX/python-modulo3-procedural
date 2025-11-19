# Mutável: Listas, dicionários
# Imutável: Tuplas, strings, números, True, False, None
# Aqui irei mostrar o problema. A solução estará no arquivo seguinte.


def lista_de_clientes(clientes_iteravel, lista=[]):  # Lista é um parâmetro mutável.
    lista.extend((clientes_iteravel))  # No final das contas, a lista não será vazia propriamente. E irá continuamente
    # concatenar os valores.
    return lista


clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(['José'])

print(clientes1)
print(clientes2)
print(clientes3)
