
def funcao(arg, arg2):
    return arg * arg2


var = funcao(2, 2)
print(var)

##########################################

a = lambda x, y: x * y  # Lamba é uma função anônima. Ou seja, não tem nome.
print(a(2, 2))

# Essa expressão acima é idêntica a expresão do início. Ambas cumprem o mesmo papel.
# Expressões lambda são úteis pra passar uma função como parâmetro para outra função.
