
import sys
import time


def tradicional():
    r = []  # Criando um array para ir adicionando de 0 a 99.
    for n in range(100):
        r.append(n)
        time.sleep(0.1)  # Simulando um programa pesado.
    return r  # Retorna o array preenchido.


t = tradicional()  # Retorna a lista para 'g'.

for v in t:  # Iterando sobre a lista preenchida.
    print(v)  # Ele espera toda o array ficar preenchido para depois exibir todos os elementos de uma vez.

print('Consumo de memória: ', sys.getsizeof(t))  # A lista consome aprox. 9KB (aprox 9000 bytes)

#####################################################
print()


def gera():  # Gerador real.
    for n in range(100):
        yield n  # 'Yield' mostra valor por valor. Como se fosse 1 'return' por vez.
        time.sleep(0.1)


g = gera()  # yield joga 1 valor de cada vez para g...

for v in g:  # ... ao mesmo tempo que v recebe 1 valor de cada vez vindo de g...
    print(v)  # ... e assim 1 valor é mostrado de cada vez.

print('Consumo de memória: ', sys.getsizeof(g))  # O consumo de memória usando apenas gerador é de apenas 112 bytes.

#####################################################
print()

print(hasattr(g, '__iter__'))  # True
print(hasattr(g, '__next__'))  # True
# g é iterador e iterável de forma simultânea. Pois todo iterador é um iterável. Mas nem todo iterável é um iterador.