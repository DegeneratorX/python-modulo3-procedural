"""
Funções Lambda

Funções lambda são funções anônimas, ou seja, funções que não são declaradas com o tradicional comando
def. Elas são criadas usando a palavra-chave lambda. As funções lambda podem ter qualquer número de argumentos, mas
apenas uma expressão. A expressão é avaliada e retornada quando a função é chamada.

Funções lambda são semelhantes às funções da matemática, onde as operações são
simples e diretas.

Suas vantagens em termos computacionais é que elas são mais leves e rápidas de serem executadas,
já que não precisam de toda a estrutura de uma função tradicional.
"""

"""
Função tradicional com def
"""

def funcao(arg, arg2):
    return arg * arg2


var = funcao(2, 2)
print("Valor do var (multiplicação):", var)

print("\n#############################################\n")

"""
Função lambda equivalente à função tradicional acima

Lê-se: função lambda que recebe os argumentos x e y e retorna x multiplicado por y.
"""

funcao_lambda = lambda x, y: x * y  # Lamba é uma função anônima. Ou seja, não tem nome.
print(funcao_lambda(2, 2), type(funcao_lambda))  # Chamando a função lambda diretamente. Note que o tipo é function.
