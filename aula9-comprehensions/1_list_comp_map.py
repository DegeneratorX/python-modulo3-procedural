"""
List Comprehension e Mapeamento (map)

List Comprehension é uma técnica do Python para criar listas de forma concisa.

Mapeamento (map) é o processo de gerar uma nova lista a partir dos elementos de outra,
podendo opcionalmente transformar esses elementos (por exemplo, copiando, alterando
ou reestruturando).

Serve para otimização e escrever menos linhas de código ao criar uma lista nova,
sem precisar manualmente popular essa lista com 'for loop' e 'append'.
"""

"""
Exemplo básico da técnica de list comprehension
"""

# Forma tradicional de criar uma lista com elementos de 0 a 9
lista_1 = []
for numero in range(10):
    lista_1.append(numero)
print("lista_1 preenchida:", lista_1)

# Mesma lista criada com list comprehension
# Lê-se: para cada número em range(10), coloque esse número na nova lista
list_comprehension_1 = [numero for numero in range(10)]
print("list_comprehension_1 criada:", list_comprehension_1)

print("\n#############################################\n")

"""
Cópia de listas e outras operações com list comprehension (mapeamento)

Posso usar list comprehension para mapear listas também.
"""

lista_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Lê-se: para cada variável em lista, coloque essa variável na nova lista.
list_comprehension_2 = [variavel for variavel in lista_2] # Mapeamento simples (cópia)
print("list_comprehension_2 criada:", list_comprehension_2)





print("\n#############################################\n")

"""
Mapeamentos com alteração utilizando list comprehension

Posso fazer operações dentro da list comprehension de forma a modificar os elementos
antes de mapear em uma nova lista.
"""

# Aqui eu digo que quero todos os elementos multiplicados por 2 nessa nova lista.
list_comprehension_3 = [variavel * 2 for variavel in lista_2]
print("list_comprehension_3 criada:", list_comprehension_3)






print("\n#############################################\n")

"""
Mapeamento de lista com múltiplos 'for'
"""
# Lê-se: para cada x em lista, para cada y em range(3), crie uma tupla (x, y).
# Entende-se que é um 'for' dentro de outro. Por isso o resultado é (1,0) (1,1) (1,2) etc.
list_comprehension_4 = [(x, y) for x in lista_2 for y in range(3)]
print("list_comprehension_4 criada:", list_comprehension_4)  






print("\n#############################################\n")

"""
Mapeamento de lista com strings
"""

lista_3 = ['Victor', 'Joao', 'Maria']
list_comprehension_5 = [v.replace('a', '@').upper() for v in lista_3]
print("list_comprehension_5 criada:", list_comprehension_5)






print("\n#############################################\n")
"""
Mapeamento de lista para inverter valores em uma tupla e transformar em dicionário
"""

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)

list_comprehension_6 = [(y, x) for x, y in tupla]  # Inverter valores e chaves nesses pares de tuplas
list_comprehension_6 = dict(list_comprehension_6)  # Bônus: converto para dicionário
print("list_comprehension_6 criada:", list_comprehension_6)





print("\n#############################################\n")
"""
Mapeamento com if em uma lista de números

Mapeamento com 'if' é o processo de gerar uma nova lista a partir de uma lista existente, 
aplicando condições para determinar quais elementos incluir ou como transformá-los.

OBSERVAÇÃO:
- Se você usar 'if' ANTES do 'for', ele é um if ternário (3 argumentos)
  e PRECISA ter 'else'.
Ex.: [expressão if condição_if else condição_else for x in iterável]
"""
lista_de_0_a_99 = list(range(100))  # Lista com 100 elementos, de 0 a 99.

# Mostra os que são divisíveis, e os que não são é substituida por NÃO.
list_comprehension_1 = [num if num % 3 == 0 else 'Não' for num in lista_de_0_a_99]  
print("list_comprehension_1 criada:", list_comprehension_1)





print("\n#############################################\n")
"""
Mapeamento para aumentar o preço dos produtos e de um único produto em uma lista de dicionários
"""

produtos = [
    {
        'nome': 'Produto 1', 
        'preco': 10.00
    },
    {
        'nome': 'Produto 2', 
        'preco': 20.00
    },
    {
        'nome': 'Produto 3', 
        'preco': 30.00
    },
]


# Quero criar uma nova lista de produtos, mas com o preço aumentado em 10%
# Lê-se: para cada produto na lista produtos, crie um novo dicionário com os mesmos dados de produto,
# mas com o preço aumentado em 10%
novos_produtos_1 = [ {**produto, 'preco': produto['preco'] * 1.1} for produto in produtos]
# "**produto" é equivalente a "'nome': produto['nome']"

print("Lista de produtos sem separador com preço aumentado em 10%:", novos_produtos_1)
print("Lista de produtos com separador com preço aumentado em 10%:", *novos_produtos_1, sep='\n')



# Perceba que eu posso usar o 'if' antes do 'for' para fazer um if ternário e escolher apenas um único elemento para modificar.
# Lê-se: para cada produto na lista produtos, se o preço do produto for maior que 20,
# crie um novo dicionário com os mesmos dados de produto, mas com o preço aumentado em 10%.
# Caso contrário, mantenha o produto original.
novos_produtos_2 = [
    {**produto, 'preco': produto['preco'] * 1.1} 
    if produto['preco'] > 20 else produto 
    for produto in produtos
]

print("Lista de produtos sem separador com preço aumentado em 10% para produtos com preço > 20:", novos_produtos_2)
print("Lista de produtos com separador com preço aumentado em 10% para produtos com preço > 20:", *novos_produtos_2, sep='\n')
