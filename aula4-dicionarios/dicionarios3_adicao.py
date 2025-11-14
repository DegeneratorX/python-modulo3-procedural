d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 4, 8): 'Tupla'
}

# Se tentar acessar e exibir uma chave que não existe, acarretará erro de exceção.
# Exemplo: print(d1['naoexiste'])
# Isso acarreta um erro. Pra resolver isso, segue o código abaixo:

if 'naoexiste' in d1:
    print(d1['naoexiste'])  # Esse código não será executado. Sem o 'if' e tentando printar, daria erro.
else:
    print("Não existe essa chave 'naoexiste' no dicionário d1. Irei adicionar agora ela.")
    d1['naoexiste'] = 'Agora existe!'

print(d1['naoexiste'])  # Agora sim não haverá erro.
print(d1)

##########################################
print()
# Existe uma forma de não precisar usar colchetes e evitar erro de qualquer jeito.
# .get() é a solução, como também foi a solução em tuplas e listas.
# Usando get e não tendo a chave no dicionário não acarreta erro, mas retorna None!
if d1.get('outra_chave_inexistente') is not None:
    print(d1.get('outra_chave_inexistente'))  # Não será executado.
else:
    print("Vamos implementar essa chave também!")
    d1['outra_chave_inexistente'] = 'Agora sim, outra chave adicionada!'
print(d1.get('outra_chave_inexistente'))
print(d1)
