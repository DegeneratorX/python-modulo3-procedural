"""
Passagem de valores (funções) para outras variáveis

É possível atribuir uma função a uma variável. Ou seja, uma variável pode receber uma função como valor.
Dessa forma, a variável poderá ser usada como se fosse a função original.
Além disso, ao atribuir uma função a uma variável, o valor retornado pela função também pode ser atribuído a essa variável.
"""


def fala_oi():
    print('Oi')
    return 2+2


fala_oi()  # Execução padrão. Irá printar 'Oi'.
variavel = fala_oi  # Atribuir uma função a outra. Ou seja...

print(type(variavel))  # Mostrará que 'variavel' é do tipo função (function).

variavel()  # ...posso passar a usar ela assim. Ela é igual a função 'fala_oi'
# Ou seja, se eu botar () na frente, ela executará da mesma forma de 'fala_oi'. Printará 'Oi'.

# Porém......

variavel_2 = fala_oi()  # Isso aqui funciona de forma completamente diferente (e também printa 'Oi').
# Ao colocar parênteses () na frente do 'fala_oi', passará o que for retornado pela função. Ou seja, 2+2 => 4.
# E a função executará ao mesmo tempo. Ou seja, exibirá 'Oi' mesmo ao atribuir o retorno para uma variável.
print(variavel_2)

print(type(variavel_2))