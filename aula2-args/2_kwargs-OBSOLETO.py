"""
Funções - **kwargs
'kwargs' é um nome convenção, um padrão da comunidade python.
Pode usar qualquer outro nome. Mas por recomendação, usa-se kwargs.
O importante é o que ** faz. 
Obs: **kwargs nada mais é que um dicionário.
"""


def func(*args, **kwargs):
    print(args)
    print(kwargs)  # Basicamente args não recebe parâmetros definidos, como nome e sobrenome. Quem recebe é o kwargs.
    print(kwargs['nome'])  # Acesso específico a um elemento de kwargs.
    print(args[0])  # Acesso específico a um elemento de args.


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]

func(*lista, *lista2, nome='Victor', sobrenome='Martins')


#############################################
print()

# O problema de usar kwargs[?] é que se a chave não for mandada pra função, por exemplo, 'nome', dará erro.
# Para resolver esse problema, podemos usar essa função:
# nome = kwargs.get('nome')


def kwargsget(*args, **kwargs):
    print(args)  # Não passou args nenhum, lista nenhuma. Portanto, tupla vazia.
    nomevictor = kwargs.get('nome')
    # IMPORTANTE: O que isso faz é basicamente: pega o valor da keyword 'nome' (get) na tupla kwargs e atribui
    # o que tiver lá dentro a uma variável. No caso atribui a 'nomevictor'
    print(nomevictor)
    idadezinha = kwargs.get('idade')
    print(idadezinha)  # Como não foi passado idade, retorna None. Se usasse índice, daria erro no compilador.
    if idadezinha is not None:  # Exemplo prático do uso do '.get()' para isso.
        print(idadezinha)
    else:
        print("Idade não existe")


kwargsget(nome='Victor', sobrenome='Martins')
