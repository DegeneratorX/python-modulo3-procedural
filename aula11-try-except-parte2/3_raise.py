"""
raise

A instrução raise é utilizada para lançar exceções de forma explícita. 
Ela pode ser usada para lançar uma exceção existente ou para criar uma nova 
exceção personalizada.
"""

def dividir(a, b):
    if b == 0:
        raise ValueError("O denominador não pode ser zero.")
    return a / b

print(dividir(8, 0))  # Isso irá lançar a exceção ValueError.



print("\n#######################################\n")
"""
Múltiplos raise

As vezes o usuário pode digitar 0 como denominador, ou um valor que não seja
numérico. Podemos usar múltiplos raise para tratar esses casos.
"""

def verifica_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (int, float)):
        raise TypeError(f'O valor {n} não é int ou float, é {tipo_n.__name__}.')
    return True

def verifica_zero(d):
    if d == 0:
        raise ValueError('O denominador não pode ser zero.')
    return True

def divide(n, d):
    verifica_int_ou_float(n)
    verifica_int_ou_float(d)
    verifica_zero(d)
    return n / d

print(divide(8, 2))      # Retorna 4.0
print(divide(8, 0))      # Lança ValueError.
print(divide(8, 'a'))    # Lança TypeError.