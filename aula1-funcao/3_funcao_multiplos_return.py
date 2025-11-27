"""
Funções mais complexas com vários parâmetros e múltiplos retornos de valores.
"""


def func(a1, a2, a3, a4, a5, nome=None, a6=None):  # a6 precisa ser default. Após um default, todos precisam também ser.
    print(a1, a2, a3, a4, a5, nome, a6)


func(1, 2, 3, 4, 5, nome='Luiz', a6='5')  # Quando se trata de default, é obrigatório definir especificamente aqui
#                                           também.

########################################
print()


def funcretorna(a1, a2, a3, nome='Victor'):
    print(a1, a2, a3)
    return nome, a1 # Quando se retorna mais de um valor, na verdade está retornando uma tupla.


var = funcretorna(1, 2, 5, nome="Zé")  # Retornará uma tupla
print("Retorno da função:", var, type(var))  # Printará o que foi retornado. Que foi a tupla.
print("Índices 0 e 1 da tupla:", var[0], var[1])  # Acesso os índices da tupla
