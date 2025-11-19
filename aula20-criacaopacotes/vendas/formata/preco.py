"""Conversão para Real"""


def real(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')
