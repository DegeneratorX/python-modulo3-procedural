tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)

ex5 = [(y, x) for x, y in tupla]  # Inverter valores e chaves nesses pares de tuplas
ex5 = dict(ex5)  # Bônus: converto para dicionário
print(ex5)

########################################
print()

l3 = list(range(100))  # Lista com 100 elementos, de 0 a 99.
ex6 = [v for v in l3 if v % 2 == 0]  # Exibe todos os múltiplos de 2.
print(ex6)

ex7 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]  # Exibe todos os múltiplos de 3 e 8 ao mesmo tempo.
print(ex7)

ex8 = [v if v % 3 == 0 else 'Não' for v in l3]  # Mostra os que são divisíveis, e os que não são é substituida por NÃO.
print(ex8)
