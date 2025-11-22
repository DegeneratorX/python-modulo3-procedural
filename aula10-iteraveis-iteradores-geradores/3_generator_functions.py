"""
Generator Functions e Yield em Python

Funções Geradoras utilizam a palavra-chave 'yield' para retornar valores um por vez, 
permitindo que a função seja pausada e retomada posteriormente.

Ele funciona como um 'return', mas ao invés de retornar de uma vez, ele retorna um valor por vez,
pausando a função até que o próximo valor seja solicitado.

Com a palavra 'yield' na função, automaticamente a função se torna geradora, e
o 'return' tradicional não pode mais ser usado para retornar valores, e sim
um 'stop iteration' para indicar o fim da iteração.
"""

"""
Implementação tradicional de uma função sem gerador
"""
def retorno_simples(n=0):
    return 1

ret = retorno_simples(n=0)
print("Tipo do retorno:", type(ret))





print("\n################################################\n")
"""
Implementação com gerador usando 'yield' (Função Geradora)
"""

def gerador_simples(n=0):
    yield 1

gen = gerador_simples(n=0)
print("Tipo do gerador:", type(gen))


# 'gen' é um gerador, portanto é um iterador, logo é um iterável
print("Provando que um gerador é um iterável com __iter__:", hasattr(gen, '__iter__'))
print("Provando que um gerador é um iterador com __next__:", hasattr(gen, '__next__'))




print("\n################################################\n")
"""
Função Geradora com return
"""

# O return em uma função geradora serve para indicar o fim da iteração.
# Com uma string, essa string será exibida na exceção StopIteration quando o gerador for esgotado.
def gerador_com_return(n=0):
    yield 1
    return 'ACABOU'

gen = gerador_com_return(n=0)
print(next(gen))  # Primeiro valor gerado
try:
    print(next(gen))  # Tentando obter o próximo valor, que não existe.
except StopIteration as e:
    print("Exceção StopIteration capturada. Valor retornado:", e.value)  # Exibe o valor retornado no return da função geradora.