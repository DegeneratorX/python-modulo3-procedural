"""
raise - usado dentro do except para apenas levantar exceção sem deixa de executar o try.
RESUMO:
Usando 'raise':
    Try é ainda considerado apesar do except. Serve para registrar erros apenas.
Não usando 'raise':
    Try é desconsiderado.

"""


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as erro:
        print(erro)
        raise  # raise irá transformar o "except" em um "registrador de erro".
        # Ou seja, o except é lançado, mas o "try" continuará sendo levado em consideração graças ao 'raise'.
        # Sem o 'raise', try é simplesmente "anulado" e desconsiderado pelo except. Com o 'raise', try ainda continuará
        # funcionando se cair no except onde o raise foi colocado.

try:
    print(divide(2, 0))
except ZeroDivisionError as erro:
    print(erro)
    # Aqui de fato como não tem 'raise', o erro foi tratado e tudo dentro do 'try' é desconsiderado.
