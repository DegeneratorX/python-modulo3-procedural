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


lista_1 = [1, 2, 3, 4, 5]
lista_2 = [10, 20, 30, 40, 50]

func(*lista_1, *lista_2, nome='Victor', sobrenome='Martins')


print("\n#############################################\n")

"""
O problema de usar kwargs[?] é que se a chave não for mandada pra função, por exemplo, 'nome', dará erro.
Para resolver esse problema, podemos usar essa função:
nome = kwargs.get('nome')
"""

def kwargsget(*args, **kwargs):
    print("Args detectado:", args)  # Não passou args nenhum, lista nenhuma. Portanto, tupla vazia.
        
    # IMPORTANTE: O que isso faz é basicamente: pega o valor da keyword 'nome' (get) na tupla kwargs e atribui
    # o que tiver lá dentro a uma variável. No caso atribui a 'nomevictor'
    nomevictor = kwargs.get('nome')
    print("Valor da chave 'nome':", nomevictor)

    idade = kwargs.get('idade')
    print("Valor da chave 'idade':", idade)  # Como não foi passado idade, retorna None. Se usasse índice, daria erro no compilador.
    if idade is not None:  # Exemplo prático do uso do '.get()' para isso.
        print("Chave 'idade' existe no dicionário kwargs, está aqui:", idade)
    else:
        print("Chave 'idade' não existe no dicionário kwargs.")


kwargsget(nome='Victor', sobrenome='Martins')

"""
Desempacotamento de dicionários com **

Ele funciona igual ao desempacotamento de listas e tuplas com *. Quando usamos
dentro de um dicionário, ele já une os dois dicionários em um só.
"""

pessoa = {
    'nome': 'Victor',
    'sobrenome': 'Martins',
}

dados_pessoa = {
    'idade': 28,
    'altuara': 1.83,
}

pessoa_completa = {**pessoa, **dados_pessoa}  # Desempacotamento de dicionários com **
print("Dicionário pessoa completa:", pessoa_completa)
