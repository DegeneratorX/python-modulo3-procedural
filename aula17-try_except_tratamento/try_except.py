"""
try-except
Tratamento de exceção: permite tratar erros e permite o programa continuar a rodar.

Usar try: e except: sem definir nomes as exceções NÃO são uma boa prática de programação.
Aqui aprendo como fazer exceções a cada tipo de classe de erros.
"""

try:
    print(a)  # 'a' não foi definido. Erro do tipo NameError na certa.
except NameError:
    print('Erro: isso aqui será executado!')

################################
print()

try:
    print(b)

except NameError as erro_fatal:  # Guardo o erro (classe) dentro de uma variável e posso ver do que se trata ao printar.
    print('Erro: isso aqui será executado, mas taqui o erro: ', erro_fatal)

except Exception as erro_fatal:  # 'Exception' nada mais é do que qualquer tipo de erro genérico, incluindo NameError.
    pass  # É como se pegasse "todo tipo de erro que sobrou" e jogasse nele.

################################
print()

try:
    c = []
    print(c[1])

except IndexError as erro_fatal:
    print('Erro de índice: ta aqui o erro: ', erro_fatal)

################################
print()
# Para tratar dois erros em um except só, usa-se tuplas com duas ou mais classes.

try:
    a = {}
    print(a[1])  # Tento acessar a chave '1'.
except (IndexError, KeyError) as erro_fatal:  # No caso o erro de fato se trata do KeyError, por se trata de uma chave.
    print("Erro, veja o que aconteceu: ", erro_fatal)
