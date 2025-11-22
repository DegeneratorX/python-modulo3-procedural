"""
Generator Functions e Yield em Python

Funções Geradoras utilizam a palavra-chave 'yield' para retornar valores um por vez, 
permitindo que a função seja pausada e retomada posteriormente.
"""


"""
Implementação tradicional sem gerador
"""

import sys
import time


def tradicional():
    lista = []  # Criando um array para ir adicionando de 0 a 30.
    for n in range(30):
        lista.append(n)
        time.sleep(0.05)  # Simulando um programa pesado.
    return lista  # Retorna o array preenchido.

lista = tradicional()  # Retorna a lista para 'lista'.

for item in lista:  # Iterando sobre a lista preenchida.
    print("Percorrendo lista: ", item)  # Ele espera toda o array ficar preenchido para depois exibir todos os elementos de uma vez.

print('Consumo de memória: ', sys.getsizeof(lista))  # A lista consome aprox. 9KB (aprox 9000 bytes)


print("\n################################################\n")
"""
Implementação com gerador usando 'yield'

O Yield é um 'return' que retorna um valor por vez, pausando a função até que o próximo valor seja solicitado.
"""


def gerador():  # Gerador real.
    for n in range(30):
        yield n  # 'Yield' mostra valor por valor. Como se fosse 1 'return' por vez.
        time.sleep(0.05)

ger = gerador()  # yield joga 1 valor de cada vez para 'ger'...

for v in ger:  # ... ao mesmo tempo que v recebe 1 valor de cada vez vindo de ger...
    print("Percorrendo gerador: ", v)  # ... e assim 1 valor é mostrado de cada vez.

print('Consumo de memória: ', sys.getsizeof(ger))  # O consumo de memória usando apenas gerador é de apenas 112 bytes.

print("\n################################################\n")
"""

"""
