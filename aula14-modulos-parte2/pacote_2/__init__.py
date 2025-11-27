"""
Esse arquivo é executado assim que o pacote é importado em 1_init.py.

Aqui vou colocar variáveis e funções que estarão disponíveis quando o pacote for 
importado. Esse arquivo "transforma" o pacote em um módulo, permitindo que
seja possível acessar diretamente essas variáveis e funções a partir do pacote.
"""
print("Você importou o pacote 'modulo_pacote_2'")

variavel_de_pacote_2 = "Variável do pacote 2"

def dobra(x):
    return x * 2