"""
Tratamento de erros com valores digitados pelo usuário e utilizando como
condicional
"""


def converte_numero(valor):
    try:
        valor = int(valor)  # Se o usuário digitar uma letra, levantará um erro.
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass  # Automaticamente a função aqui retorna None.


while True:
    numero = converte_numero(input('Digite um número: '))

    if numero is None:  # Se a função retornar None...
        print('Erro: isso não é um número.')
    else:
        print(numero*5)
