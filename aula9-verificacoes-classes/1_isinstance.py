"""
isinstance

Método que verifica se um objeto é uma instância de uma classe ou de uma tupla de classes.
"""

lista = [
    'a', 1, 1.1, True, [0,1,2], (3,4,5), {0,1}, {'nome': 'Victor'}, None
]

for item in lista:
    if isinstance(item, set):
        print(f'O item {item} é um set.')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print(f'O item {item} é uma string.')
        print(item.upper(), isinstance(item, str))

    elif isinstance(item, (int, float)):
        print(f'O item {item} é um número.')
        print(item * 3, isinstance(item, (int, float)))

    else:
        print(f'O item {item} é de um tipo não tratado.')
    print("\n#######################################\n")