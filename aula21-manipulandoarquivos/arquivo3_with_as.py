"""
Alternativa ao try except

Eu não preciso mandar fechar o arquivo.
Esse gerenciador de contexto abre o arquivo e fecha depois de forma automática.
"""

# file = open(...) equivalente.
with open('abc.txt', 'w+') as file:  # Função pra abrir o arquivo + variável para trabalhar a escrita e leitura.
    file.write('Linha1\n')
    file.write('Linha2\n')
    file.write('Linha3\n')

    file.seek(0)

    print(file.read())
