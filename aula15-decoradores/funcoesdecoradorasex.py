"""
Funções de maior grandeza - Higher Order Functions - HOF

Quando uma linguagm suporta HOF, indica que podemos ter funções que retornam
outras funções como resultado ou mesmo que podemos passar funções como argumentos
para outras funções, e até mesmo criar variáveis do tipo de funções nos nossos programas.
"""


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print(calcular(4, 3, somar))

print(calcular(4, 3, diminuir))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))
