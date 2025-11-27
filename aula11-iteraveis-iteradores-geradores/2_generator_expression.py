"""
Generator

São funções que sabem pausar em determinado local do programa, e retomar dali sempre que o próximo valor for solicitado.

Todo generator é um iterador. Mas um iterator não é um generator.

A importância dos generators é a economia de memória, porém com custo maior de processamento.
Nós não precisamos de todos os valores ao mesmo tempo de uma lista em casos específicos, e caso a lista
seja enorme, o generator pode ser uma ótima solução para pegar um dado por vez, sem precisar carregar tudo na memória.
"""

import sys # Importa o módulo sys para usar a função getsizeof(), que retorna o tamanho em bytes de um objeto na memória.

lista_1 = list(range(10))
print("Tamanho da lista_1 em bytes:", sys.getsizeof(lista_1), "bytes.")  # getsizeof(obj) retorna o número de bytes que o obj consome da memória.

lista_2 = list(range(1000))  # Usando lista maior. Maior o consumo de memória.
print("Tamanho da lista_2 em bytes:", sys.getsizeof(lista_2), "bytes.")





print("\n########################################################\n")
"""
Generator Expression

Sintaxe semelhante à list comprehension, mas usando parênteses () ao invés de colchetes [].

A ideia é gerar os valores sob demanda, ou seja, um por vez, sem precisar armazenar todos na memória.
"""


lista_3 = [n for n in range(30)]  # List Comprehension
generator = (n for n in range(30))  # Generator Expression

print("Tamanho da lista_3 em bytes:", sys.getsizeof(lista_3), "bytes.") # Tamanho da lista na memória.
print("Tamanho do generator em bytes:", sys.getsizeof(generator), "bytes.") # Tamanho do generator na memória. Muito menor que a lista.

print("Printando lista_3:", lista_3) # Exibe todos os valores da lista.
print("Printando generator:", generator) # Note que o generator não exibe os valores diretamente, e sim o local do objeto na memória.


print("Gerando valores do generator:")
for n in generator:
    print(n, end=" ")  # Exibe cada valor do generator, um por vez.


print("\nNote que após o 'for' acima, o generator já foi esgotado e não possui mais valores.")
for n in generator:
    print(n)  # Não exibe nada, pois o generator já foi esgotado no 'for loop' anterior.
    print("Isso não será exibido.")


# Por fim, não é possível acessar índices em um generator, pois ele não suporta indexação.
try:
    print(generator[10])  # Tentando acessar o índice 10 do generator.
except TypeError as e:
    print("Erro:", e)