"""
Dicionarios - muito similar a lista

Nas listas o python gera um índice pra você
No dicionário, você controla o índice (normalmente chamado Chave).
Ou seja, o dicionário é uma estrutura de dado que suporta um par de chave e um valor.
Em estruturas de dados, isso é chamado de 'mapa' ou 'hashmap' em outras linguagens.
Em aplicações de desenvolvimento, são semelhantes a objetos em JavaScript (JSON).
"""

d1 = {'chave1': 'valor da chave1', 'chave2': 30}  # Criação de um dicionário

print(d1)  # Tipo 'dict'.
print(type(d1))

d1['nova_chave'] = 'Valor da nova chave'  # Adicionar elemento a um dicionário.

print("Dicionário d1: ",d1)
print("Valor da chave1: ",d1['chave1'])  # Acesso a um valor específico de um dicionário. Bem parecido com listas.


print("\n############################################\n")

"""
Outra forma de criar dicionários
"""

d2 = dict(chave1='Valor da chave', chave2='Valor de outra chave')
d2['nova_chave'] = 'Valor da nova chave'

print("Dicionário d2: ",d2)

print("\n############################################\n")

"""
Dicionarios - Chaves Duplicadas
"""

d3 = {
    'chave': 'valor 1', 
    'chave': 'valor 2', 
    'chave': 'valor real da chave'
}

print("Dicionário d3: ",d3)  # Em casos de chaves duplicadas, mostrará a última chave atribuida. No caso, mostrará o 'valor real da chave'.

d4 = {1: 'valor1', 2: 'valor2', 3: 'valor3'}

print("Dicionário d4: ",d4)  # Agora sim exibirá cada valor, pois as chaves são todas diferentes.
print("Valor da chave 3: ",d4[3])  # Acesso a um valor específico do dicionário.




print("\n############################################\n")



"""
Acesso a chaves que não existem
"""

d5 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 4, 8): 'Tupla'
}

# Se tentar acessar e exibir uma chave que não existe, acarretará erro de exceção.
# Exemplo: print(d1['naoexiste'])
# Isso acarreta um erro. Pra resolver isso, segue o código abaixo:

if 'naoexiste' in d5:
    print(d5['naoexiste'])  # Esse código não será executado. Sem o 'if' e tentando printar, daria erro.
else:
    print("Não existe essa chave 'naoexiste' no dicionário d5. Irei adicionar agora ela.")
    d5['naoexiste'] = 'Agora existe!'
print("Valor de d5['naoexiste']", d5['naoexiste'])  # Agora sim não haverá erro.
print("Dicionário d5:", d5)

# Para evitar KeyError ao acessar chaves que podem não existir, pode-se usar também o método .get()
print(d5.get('naoexiste_nem_a_pau', 'padrão'))  # retorna 'padrão' se não existir

print("\n############################################\n")


"""
Acesso a chaves de tipos variados (imutáveis)

OBS: As chaves podem ser de tipos variados, MAS devem ser imutáveis. Exemplo: strings, números (int, float, etc) e tuplas.
"""

# Para tentar acessar chaves que são imutáveis, segue o código abaixo:
# Usando os tipos das chaves
print(d5['str'])          # chave string
print(d5[123])            # chave int
print(d5[(1, 2, 4, 8)])   # chave tuple


chave = (1, 2, 4, 7)
if chave in d5:
    print(d5[chave])