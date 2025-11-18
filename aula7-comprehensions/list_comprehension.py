"""
List Comprehension

Serve para otimização e escrever menos linhas de código.
"""

"""
Exemplo básico de list comprehension
"""

lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Lê-se: para cada variável em lista, coloque essa variável na nova lista.
list_comprehension_1 = [variavel for variavel in lista_1]
print("list_comprehension_1 criada:", list_comprehension_1)

# Aqui eu digo que quero todos os elementos multiplicados por 2 nessa nova lista.
list_comprehension_2 = [variavel * 2 for variavel in lista_1]

# Lê-se: para cada x em lista, para cada y em range(3), crie uma tupla (x, y).
# Entende-se que é um 'for' dentro de outro. Por isso o resultado é (1,0) (1,1) (1,2) etc.
list_comprehension_3 = [(x, y) for x in lista_1 for y in range(3)]
print("list_comprehension_3 criada:", list_comprehension_3)  


print("\n#############################################\n")

"""
Exemplo mais complexo de list comprehension com strings
"""

lista_2 = ['Victor', 'Joao', 'Maria']
list_comprehension_4 = [v.replace('a', '@').upper() for v in lista_2]
print("list_comprehension_4 criada:", list_comprehension_4)
