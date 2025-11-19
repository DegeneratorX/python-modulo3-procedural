# Mutável: Listas, dicionários
# Imutável: Tuplas, strings, números, True, False, None


def lista_de_clientes(clientes_iteravel, lista=None):  # Pra solucionar, eu atribuo None, parâmetro imutável.
    if lista is None:  # Se for none...
        lista = []  # Esvazio a lista.
    lista.extend(clientes_iteravel)  # Agora sim tenho uma lista limpa e posso printar diferentes valores.
    return lista


clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(['José'])

print(clientes1)
print(clientes2)
print(clientes3)
