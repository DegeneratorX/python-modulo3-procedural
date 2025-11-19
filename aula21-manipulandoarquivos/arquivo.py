"""
'r' = abrir pra ler (default)
'w' = abrir para escrever,
'x' = abre para criação exclusiva, e falha se o arquivo já existe
'a' = abre para escrever, acrescentando no final do arquivo se ele existe
'b' = modo binário
't' = modo texto (default)
'+' = deleta tudo do arquivo para ler e escrever

https://docs.python.org/3/library/functions.html#open
"""

file = open('abc.txt', 'w+')
# Criação de um arquivo limpo chamado abc.txt na mesma pasta.

file.write('Linha1\n')  # Escrita no arquivo.
file.write('Linha2\n')
file.write('Linha3\n')  # O cursor que pisca e escreve (barra, |) está no final do arquivo.

file.seek(0, 0)  # O comando .seek() coloca o cursor | de volta pro começo.
# O primeiro zero indica pra voltar pra estaca 0 do arquivo. O segundo zero é uma referência q n precisa saber por hora.

print('Lendo linhas: ')
print(file.read())  # Com o cursor | no começo, ele irá percorrer o arquivo e irá ler ele por inteiro.
print('#'*15)

file.seek(0, 0)  # Colocando novamente o cursor no começo do arquivo.

print(file.readline(), end='')  # Lê linha por linha. O cursor vai pro final da linha 1. end='' para n quebrar linha.
print(file.readline(), end='')  # O cursor começa no final da primeira linha e vai até o final da segunda linha.
print(file.readline(), end='')
print('#'*15)

file.seek(0, 0)
print(file.readlines())  # .readlines() no plural cria uma lista com cada linha lida.

file.close()  # Fecha o arquivo.

