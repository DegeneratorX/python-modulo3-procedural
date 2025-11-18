"""
Ordenar listas com lambda

.sort() e sorted() normalmente não entendem como ordenar qualquer dentro de lista.
"""

"""
Ordenação de Dicionário com lambda
"""

def ordena_dict(item):
    return item['sobrenome']  # Escolhe a chave 'sobrenome' para ordenar.

lista_com_dicionarios = [
    {'nome': 'Luiz', 'sobrenome': 'Oliveira'},
    {'nome': 'Maria', 'sobrenome': 'Silva'},
    {'nome': 'Ana', 'sobrenome': 'Souza'},
    {'nome': 'João', 'sobrenome': 'Pereira'},
    {'nome': 'Eduardo', 'sobrenome': 'Alves'},
]


# Usando função tradicional para ordenar a lista
lista_com_dicionarios_ordenada_funcao = sorted(lista_com_dicionarios, key=ordena_dict)  # Ordena a lista com base na função ordena.
print("Lista ordenada por sobrenome usando função tradicional:", lista_com_dicionarios_ordenada_funcao)

# Usando lambda para ordenar a mesma lista
lista_com_dicionarios_ordenada_lambda = sorted(lista_com_dicionarios, key=lambda item: item['sobrenome'])  # Ordena a lista com base na função lambda.
print("Lista ordenada por sobrenome usando lambda:", lista_com_dicionarios_ordenada_lambda)


print("\n#############################################\n")

"""
Ordenação de listas ou tuplas com lambda
"""

def ordena_lista(item):
    return item[1]  # Escolho o índice 1 da lista (de 0 a 1) para ordenar. Ou seja, os preços.

#  Exemplo: produtos, preços
lista = [
    ['P1', 13],
    ['P3', 7],
    ['P5', 8],
    ['P4', 50],
    ['P2', 6],
]


# Usando função tradicional para ordenar a lista
lista_com_listas_ordenada_funcao = sorted(lista, key=ordena_lista, reverse=True)  # Baseado no que retorna na função, ele ordena. Reverse ordena ao contrário.
print("Lista ordenada por preço usando função tradicional:", lista_com_listas_ordenada_funcao)

# Usando lambda para ordenar a mesma lista
lista_com_listas_ordenada_lambda = sorted(lista, key=lambda item: item[1], reverse=True)  # Baseado no que retorna na função, ele ordena. Reverse ordena ao contrário.
print("Lista ordenada por preço usando lambda:", lista_com_listas_ordenada_lambda)