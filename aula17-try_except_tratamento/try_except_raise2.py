"""
Lançamento de exceção usando raise
"""


def divide(n1, n2):
    if n2 == 0:
        raise ValueError("N2 não pode ser 0.")  # Criando a minha própria exceção, mesmo não sendo ZeroDivisionError.
    return n1 / n2


try:
    print(divide(n1=2, n2=0))
except ValueError as error:
    print('Você está tentando dividir por 0.')
    print(error)  # Printará "N2 não pode ser zero".
