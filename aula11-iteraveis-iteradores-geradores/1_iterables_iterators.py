"""
Iteráveis e Iteradores em Python

Um iterável é um objeto que você pode iterar sobre ele, mas ele não vai dar um valor de cada vez.

Um iterador sempre vai te dar um valor de cada vez sempre que preciso.

Um iterável não necessariamente é um iterador. Mas todo iterador é um iterável.
"""


"""
Iteráveis em Python

Iterável é tudo aquilo que pode ser "percorrido" (ou iterado). Exemplos: listas, strings, dicionários, arquivos, etc.

Iteráveis são os objetos que são iterados. Um objeto é considerado iterável se possuir o método mágico '__iter__'.
"""

lista_1 = [0, 1, 2, 3, 4, 5]
numero = 1234
string = 'String'
    
# '__iter__' é um método mágico que identifica se um objeto é iterável. Se a classe do objeto possuir esse método, o objeto é iterável.
print("Verificando se uma lista é iterável:", hasattr(lista_1, '__iter__'))
print("Verificando se um número é iterável:", hasattr(numero, '__iter__'))
print("Verificando se uma string é iterável:", hasattr(string, '__iter__'))





print("\n##############################################\n")
"""
Iteradores em Python

Iterador é tudo aquilo que pode permitir a iteração (ou seja, o ato de percorrer os elementos) de um objeto iterável. 
Exemplos: objetos retornados por funções como iter(), range(), map(), filter(), etc.

Iteradores são os objetos que fazem a iteração propriamente dita. Um objeto é considerado um iterador se possuir o método mágico '__next__'.
Pode possuir também o método '__iter__', mas o que define um iterador é o método '__next__'.
"""

lista_2 = [15, 30, 45, 60, 75]

# O que o laço 'for loop' faz é transformar um objeto iterável em iterador. Então ele utiliza o iterador para exibir cada valor linha por linha.
for i in lista_2:
    print("Iterando em lista:", i)


# '__next__' é um método mágico que identifica se um objeto é um iterador. Se a classe do objeto possuir esse método, o objeto é um iterador.
print("Verificando se uma lista é um iterador:", hasattr(lista_2, '__next__'))
print("Transformando a lista em um iterador...")
lista_2 = iter(lista_2)  # Conversão de um iterável para um iterador.
print("Verificando se a lista é um iterador agora:", hasattr(lista_2, '__next__'))


# Agora posso usar a função next() em 'lista_2', já que agora 'lista_2' é um iterador.
# Sem a conversão para um iterador usando iter(), as linhas abaixo dariam erro.
print("Passo 0", next(lista_2))
print("Passo 1", next(lista_2))
print("Passo 2", next(lista_2))
print("Passo 3", next(lista_2))
print("Passo 4", next(lista_2))

try:
    print("Passo 5", next(lista_2))  # Aqui dará erro, pois não há mais elementos na lista.
except StopIteration:
    print("StopIteration: não há mais elementos para iterar.")
    print("Aqui simulamos um laço for, que lida automaticamente com a exceção StopIteration.")