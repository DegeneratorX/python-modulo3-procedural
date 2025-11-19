"""
O for temporariamente converte a nossa variável iterável (string, tupla, lista...)
em um iterador. E a cada iteração, ele automaticamente dá um next().

Ele também trata exceções de forma automática, e quando chega no fim da iteração,
se não houver mais índices iteráveis, o 'for' termina.
"""

nome = "Victor"
iterador = iter(nome)

try:  # Teoricamente na 7° iteração é pra dar exceção. Mas o except é acionado caso ocorra.
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))

except:
    pass  # E é exatamente isso que o for faz de forma completamente automática.

###################################
#  Isso acima é a mesma coisa que:
#
#  for v in nome:
#       print(v)
###################################

