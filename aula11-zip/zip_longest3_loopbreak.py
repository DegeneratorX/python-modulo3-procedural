from itertools import count

indice = count()

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(indice, estados, cidades)  # Combinando os 3 iteráveis. Lembrando de retirar o fillvalue=, pois
#                                                  não é parâmetro de zip().

for indice, estados, cidades in cidades_estados:  # Desempacotamento de uma tupla
    print(indice, estados, cidades)
# Por pegar o menor iterável como referência, irá parar em BA (índice 2)
