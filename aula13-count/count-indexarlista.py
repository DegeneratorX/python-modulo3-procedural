from itertools import count

contador = count()

lista = ['Luiz', 'Joao', 'Maria']

novo_na_lista = input("Digite qualquer coisa: ")
lista.append(novo_na_lista)
print(list(lista))

lista = zip(contador, lista)
print(list(lista))  # Adiciono índices para cada elemento de uma lista de forma automática.
# Posso combinar isso com o append + input. Ou seja, adiciono novos elementos a uma lista e elas serão
# automaticamente indexadas!


