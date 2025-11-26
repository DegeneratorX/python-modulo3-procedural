"""
Yield em Python

Funções que utilizam a palavra-chave 'yield' são chamadas de Funções Geradoras. Elas retornam valores um por vez, 
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




print("\n################################################\n")
"""
Usando 'yield' em uma função mais complexa

O Yield é um 'return' que retorna um valor por vez, pausando a função até que o próximo valor seja solicitado.

Nesse cenário simulamos um programa pesado que demora para processar cada valor. Isso implica em:
- Sem gerador, a lista precisa ser preenchida totalmente antes de mostrar seus valores de uma vez;
- Enquanto o gerador já vai mostrando os valores conforme são processados. Isso além
de economizar memória, melhora a performance do programa e tem aplicações em
situações práticas onde os dados precisam ser obtidos em tempo real.
"""

import sys
import time


def tradicional():
    l1 = []  # Criando um array para ir adicionando de 0 a 30.
    for n in range(30):
        l1.append(n)
        time.sleep(0.1) # Simulando um processamento demorado.
    return l1  # Retorna o array preenchido.


l1 = tradicional()  # Retorna a lista para 'l1'.
print("\n#### Printando a lista sem gerador ####")
for item in l1:  # Iterando sobre a lista preenchida.
    print("Percorrendo lista: ", item)  # Ele espera toda o array ficar preenchido para depois exibir todos os elementos de uma vez.

print('Consumo de memória: ', sys.getsizeof(l1))  # A lista consome aprox. 312 bytes (pode variar).




def gerador():  # Gerador real.
    for n in range(30):
        yield n  # 'yield' mostra valor por valor. Como se fosse 1 'return' por vez.
        time.sleep(0.1)

ger = gerador()  # yield joga 1 valor de cada vez para 'ger'...

print("\n#### Printando com gerador ####")
for v in ger:  # ... ao mesmo tempo que v recebe 1 valor de cada vez vindo de ger...
    print("Percorrendo gerador: ", v)  # ... e assim 1 valor é mostrado de cada vez.

print('Consumo de memória: ', sys.getsizeof(ger))  # O consumo de memória usando apenas gerador é de apenas 104 bytes (pode variar).