"""
Global - palavra-chave

A palavra-chave 'global' é usada para declarar que uma variável dentro de uma função 
refere-se a uma variável global. Isso permite que a função modifique a variável global 
em vez de criar uma nova variável local.

Sem Global, a variável seria tratada como uma nova variável local dentro da função,
e só poderia ser lida, não modificada.
"""

variavel_global = 'valor'  # Considera-se variável global por vir antes das funções.


def func():
    print(variavel_global)


def func2():
    variavel_global = 'Outro valor'  # Substitui temporariamente a variável
    print(variavel_global)


def func3():
    global variavel_global
    variavel_global = 'Mais outro valor'
    print(variavel_global)


func()
func2()
print(variavel_global)  # Lembra que modifiquei 'variavel_global'? Saiu da 'func2, e voltou a ter seu valor global original
func3()
print(variavel_global) # Graças à keyword 'global', alterou a variável pra sempre, mesmo na função.






print("\n#########################################\n")
"""
O problema é que isso não é uma boa prática da programação. Existe uma solução melhor e otimizada.
"""

def func4(frase):
    frase = 'Agora sim, essa forma é decente'
    return frase


outra_variavel_global = func4(variavel_global)
print(outra_variavel_global)  # Essa forma é melhor, pois não altera a variável global diretamente.