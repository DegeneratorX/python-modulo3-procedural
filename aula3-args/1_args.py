"""
Funções - *args
'args' é um nome convenção, um padrão da comunidade python.
Pode usar qualquer outro nome. Mas por recomendação, usa-se args.
O importante é o que * faz. 
Obs: *args nada mais é que uma tupla.
"""

# lista = [1,2,3,4,5]
# n1, n2, *n = lista  <-- Desempacotamento, rever aula sobre isso.
# print(n1, n2, n)  <-- Printará 1, 2 e a lista [3, 4, 5]


def func(*args):
    print(args)
    print(args[0])  # Acessando o primeiro valor da tupla
    print(args[-1])  # Acessando o último valor da tupla
    print(len(args))  # Quantidade de argumentos/elementos na tupla.


# DESEMPACOTAMENTO
lista = [1, 2, 3, 4, 5]
print(*lista) # Desempacotando a lista através do print. Exibirá 1 2 3 4 5. Isso é equivalente a print(1, 2, 3, 4, 5).

# EMPACOTAMENTO
func(1, 2, 3, 4, 5)  # Manda todos esses valores para *args e empacota eles em uma tupla.

print("\n############################################\n")


"""
Função que tenta alterar o primeiro valor de args.
"""
def func_2(*args):
    # args[0] = 20  <-- É impossível alterar uma tupla. Descomentando isso acarretaria ao erro.
    args = list(args)  # Mas... convertendo em lista, agora sim é possível alterar valores dos índices.
    args[0] = 20
    print(args)  # Exibirá [20, 2, 3, 4, 5]


func_2(1, 2, 3, 4, 5)


print("\n############################################\n")

"""
Função que percorre os valores de args.
"""
def argsfor(*args):
    for valor in args:
        print(valor)  # Como foi empacotado em uma tupla, 1,2,3,4,5 será percorrido e exibido cada um.


argsfor(1, 2, 3, 4, 5)

print("\n############################################\n")

"""
Função que recebe uma tupla ou lista como argumento e desempacota ela com *args.
"""
def argstuplalista(*args):
    print(args)  # Irá printar uma tupla ou lista empacotada em uma tupla.


tupla = 1, 2, 3, 4, 5  # Tupla implícita
lista = [1, 2, 3, 4, 5]
print("Printando a tupla:", tupla)  # Será uma tupla (1,2,3,4,5).
print("Printando a lista:", lista)  # Será uma lista [1,2,3,4,5]

argstuplalista(tupla) # Irá printar a tupla empacotada.
argstuplalista(lista) # Irá printar a lista empacotada.
argstuplalista(lista, '6')  # Irá printar a lista empacotada e o valor '6' como uma tupla com dois elementos.
argstuplalista(*lista, '6', 7, "ZÉ")  # Mando a lista desempacotada e *args empacota novamente tudo, resultando em uma tupla única com 8 elementos.

lista2 = [10, 20, 30, 40, 50]
argstuplalista(*lista, *lista2)  # Desempacota tudo e depois reempacota na função pelo *args. Tudo vira uma tupla só, com 10 elementos.
