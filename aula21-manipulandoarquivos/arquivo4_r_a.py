import os

with open('abc.txt', 'r') as file:  # lê arquivo apenas
    # file.write('Linha1\n') << Como só abri pra leitura usando 'r', isso daria erro.
    print(file.read())

with open('abc.txt', 'a+') as file:  # 'a' coloca o cursor no final.
    file.write('Outra Linha!')
    file.seek(0)
    print(file.read())

###################################
# os.remove('abc.txt')
# Deleta o arquivo por completo!
###################################
