"""
Ao importar esse módulo inteiro para o arquivo aplicativo.py, tudo será executado.
"""

import math

PI = math.pi


def dobra_lista(lista):
    return [x*2 for x in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r


print(__name__)  # Isso será executado mesmo indo para o outro arquivo.
# Se executado no arquivo 'aplicativo.py', mostrará o nome do módulo 'calculos'.
# Se executado aqui mesmo, mostrará '__main__'.

if __name__ == '__main__':  # Portanto, uma condicional é necessária para evitar que esse código todo seja executado lá.
    lista = [1, 2, 3, 4, 5]
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)
