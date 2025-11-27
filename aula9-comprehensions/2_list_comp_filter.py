"""
Filtro (filter) de dados em uma lista

- Filtro (filter) é o processo de selecionar elementos de uma lista com base em condições
  específicas, resultando em uma nova lista que contém apenas os elementos que atendem a essas condições.

Isso pode ser feito de forma tradicional, mas podemos usar list comprehension para filtrar 
dados de uma lista para outra.

- TUDO que vier ANTES do 'for' é a expressão que define o que será mapeado na nova lista.
- TUDO que vier DEPOIS do 'for' é a parte que define o filtro (condição) para incluir
  ou excluir elementos da nova lista.

OBSERVAÇÃO:
- Se você usar 'if' DEPOIS do 'for', ele é um filtro e NÃO pode ter 'else'.
  Ex.: [expressão for x in iterável if condição_if]
"""


"""
Filtro de dados em uma lista simples usando list comprehension

O filtro é um 'if' que vem DEPOIS do 'for' na list comprehension.
"""

lista_de_0_a_99 = list(range(100))  # Lista de 0 a 99

# Exibe todos os múltiplos de 2.
lista_1 = [num for num in lista_de_0_a_99 if num % 2 == 0] 
print("lista_1 criada:", lista_1)

# Exibe todos os múltiplos de 3 e 8 ao mesmo tempo.
lista_2 = [num for num in lista_de_0_a_99 if num % 3 == 0 if num % 8 == 0]  
print("lista_2 criada:", lista_2)




print("\n#############################################\n")

"""
Filtro de dados em uma lista simples com múltiplas condições usando list comprehension
"""

lista_de_0_a_9 = [n for n in range(10)]  # Lista de 0 a 9
# Quero criar uma nova lista apenas com os números menores que 5 e que sejam pares.
lista_4 = [n for n in lista_de_0_a_9 if n < 5 and n % 2 == 0]

print("Lista de 0 a 9:", lista_de_0_a_9)
print("Lista de números menores que 5 e pares:", lista_4)




print("\n#############################################\n")
"""
Filtro de dados em uma lista de dicionários usando list comprehension
"""

produtos_2 = [
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
    {
        'nome': 'Produto 4', 
        'preco': 5.00
    },
    {
        'nome': 'Produto 5',
        'preco': 15.00
    },
    {
        'nome': 'Produto 6',
        'preco': 25.00
    },
    {
        'nome': 'Produto 7',
        'preco': 423.00
    },
    {
        'nome': 'Produto 8',
        'preco': 8.00
    }
]

# Lê-se: para cada produto na lista produtos_2, se o preço do produto for maior ou igual a 20, 
# e o preço aumentado em 10% for maior que 10, crie um novo dicionário com os mesmos dados de 
# produto, mas com o preço aumentado em 10%.
novos_produtos_3 = [
    {**produto, 'preco': produto['preco'] * 1.1}
    for produto in produtos_2
    if produto['preco'] >= 20 and produto['preco'] * 1.1 > 10
]

print("Lista de produtos com preço aumentado em 10% apenas para produtos com preço >= 20 e novo preço > 10:", novos_produtos_3)





print("\n#############################################\n")
"""
Mapeamento com condicional 'if' e filtro juntos em uma list comprehension
"""

# Lê-se: para cada produto na lista produtos_2, se o preço do produto for maior que 20, 
# crie um novo dicionário com os mesmos dados de produto, mas com o preço aumentado em 10%.
# Apenas inclua esse produto na nova lista se o novo preço for maior que 10.
novos_produtos_4 = [
    {**produto, 'preco': produto['preco'] * 1.1}
    if produto['preco'] > 10 else {**produto}
    for produto in produtos_2
    if produto['preco'] > 20 and produto['preco'] * 1.1 > 10
]

print(f"Lista de produtos com preço aumentado em 10% apenas para produtos com preço >= 20 e novo preço > 10 (map + filter): {novos_produtos_4}")


# Um código 100% equivalente ao acima seria:
novos_produtos_5 = []
for produto in produtos_2:
    # filtro
    if produto['preco'] > 20 and produto['preco'] * 1.1 > 10:
        # map
        if produto['preco'] > 10:
            novo_produto = {**produto, 'preco': produto['preco'] * 1.1}
        else:
            novo_produto = {**produto}
        novos_produtos_5.append(novo_produto)

print(
    "Lista de produtos (código tradicional) com preço aumentado em 10% apenas "
    "para produtos com preço >= 20 e novo preço > 10 (map + filter explícito):",
    novos_produtos_5
)