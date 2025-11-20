"""
dir(), hasattr() e getattr() em Python

- dir(): função que retorna uma lista com os atributos e métodos de um objeto.
- hasattr(): função que verifica se um objeto possui um determinado atributo ou método.
- getattr(): função que retorna o valor de um atributo de um objeto.
- setattr(): função que define o valor de um atributo de um objeto.
"""

"""
dir()

Muito útil para quando queremos saber quais são os atributos/métodos de um objeto.
A função dir() retorna uma lista com esses atributos/métodos. Nem sempre a IDE
ou editor de texto mostra todos os atributos/métodos de um objeto, então o dir()
mostra com garantia todos eles.
"""

print(dir([]))  # Lista de atributos/métodos do objeto lista.
print(dir(''))  # Lista de atributos/métodos do objeto string.
print(dir({}))  # Lista de atributos/métodos do objeto dicionário.


print("\n#######################################\n")
"""
hasattr()

A função hasattr() recebe dois parâmetros: o objeto e uma string com o nome do
atributo/método. Retorna True se o atributo/método existir no objeto e False
caso não exista.
"""

string = 'Victor'
metodo = 'upper'

if hasattr(string, metodo):
    print(f'A string possui o método {metodo}.')
    print(string.upper())  # Chamada do método.
else:
    print(f'A string não possui o método {metodo}.')



print("\n#######################################\n")
"""
getattr()

A função getattr() recebe dois parâmetros: o objeto e uma string com o nome do
atributo/método. Retorna o valor do atributo ou o método (sem os parênteses).
"""

if hasattr(string, metodo):
    print(f'A string possui o método {metodo}.')
    metodo_upper = getattr(string, metodo)  # Pega o método 'upper' da string.
    print(metodo_upper())  # Chama o método.
else:
    print(f'A string não possui o método {metodo}.')




print("\n#######################################\n")
"""
setattr()

A função setattr() recebe três parâmetros: o objeto, uma string com o nome do
atributo e o valor a ser atribuído. Se o atributo existir, seu valor será
atualizado. Se não existir, o atributo será criado com o valor fornecido.

OBSERVAÇÃO: O setattr() só funciona em objetos que permitem a criação de
atributos dinâmicos, como objetos de classes criadas pelo usuário. Não funciona
em objetos de classes internas do Python, como listas, strings, dicionários, etc.
"""

class MinhaClasse:
    pass

obj = MinhaClasse()

if hasattr(obj, 'nova_variavel'):
    print('Atributo já existe.')
else:
    setattr(obj, 'nova_variavel', 'Valor da nova variável.')
    print('Atributo criado com sucesso.')

print(hasattr(obj, 'nova_variavel'))
print(getattr(obj, 'nova_variavel'))
