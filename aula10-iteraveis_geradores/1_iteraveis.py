"""
Iteráveis em Python

Iteráveis: tudo aquilo que pode ser "percorrido" (ou iterado). Exemplos: listas, strings, dicionários, arquivos, etc.
"""

lista = [0, 1, 2, 3, 4, 5]
numero = 1234
string = 'String'

print(hasattr(lista, '__iter__'))  # hasattr(variável, '__iter__') verifica se a variável é uma iterável.
#                                    Retorna True ou False. Nesse caso aqui, True.
print(hasattr(numero, '__iter__'))  # Retornará False, pois, um número não é um objeto iterável.
print(hasattr(string, '__iter__'))  # String é um obj iterável. True.
# '__iter__' é um parâmetro detector de variáveis iteráveis.

for v in lista:
    print(v)  # O que o For faz é transformar um objeto iterável em iterador.
#               Então ele utiliza o iterador para exibir cada valor linha por linha.

# Para checar se um objeto é iterador, utiliza-se:
print(hasattr(lista, '__next__'))  # Implicará em False, pois 'lista' é iterável, não iterador.

