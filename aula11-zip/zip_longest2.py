"""
Zip - Unindo Iteráveis
Zip_longest - Itertools
"""

from itertools import zip_longest, count
#  Importando as funções zip_longest() e count().

indice = count()  # Contador que gera números do 0 até o infinito em tempo real (não é de uma vez!!!!!!).
#                   Ou seja, count() é um gerador! Retorna 1 índice por vez.
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip_longest(indice, estados, cidades, fillvalue='Estado')  # Combinando os 3 iteráveis

for indice, estados, cidades in cidades_estados:  # Desempacotamento de uma tupla
    print(indice, estados, cidades)  # Geração de índices infinitos. Cancelar o programa ou travará!

# O motivo de gerar de forma infinita é pq o zip_longest, como já se sabe, pega o maior iterável (tupla, lista) e usa
# como referência.
# Os valores que não tiverem pareados, aparecerá None.

# Para solucionar o problema, basta usar zip() apenas, e o menor iterável será usado como referência, e assim
# irá parar em BA (count 2). Isso é demonstrado no próximo arquivo.
