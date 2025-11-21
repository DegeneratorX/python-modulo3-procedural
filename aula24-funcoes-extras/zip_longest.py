"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
# Não se preocupar com isso abaixo agora. Estou apenas passando a função zip_longest() do módulo Itertools.
# A alternativa seria usar itertools.zip_longest(estados, cidades) no próprio código.

from itertools import zip_longest

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Ratanabá']
estados = ['SP', 'MG', 'BA']

cidades_estados1 = zip_longest(estados, cidades)
print(list(cidades_estados1))

# Também posso substituir o None por algum valor default.

cidades_estados2 = zip_longest(estados, cidades, fillvalue='Estado não encontrado')
print(list(cidades_estados2))
