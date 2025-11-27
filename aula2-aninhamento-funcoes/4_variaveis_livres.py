"""
Variáveis Livres, 'locals()', 'globals()' e '__code__.co_freevars'

Variáveis livres são aquelas que não são definidas dentro do escopo local de uma função,
mas são referenciadas dentro dela. Essas variáveis são geralmente definidas em um escopo
externo à função, como em uma função envolvente (função externa) ou no esc

- globals() mostra todas as variáveis globais do escopo atual.
- locals() mostra todas as variáveis locais do escopo atual.
- __code__.co_freevars de uma função retorna uma tupla com os nomes das variáveis livres
utilizadas dentro dessa função.
"""



"""
A variável 'a' (dentro do escopo da função 'dentro') é uma variável livre, pois 
ela não está definida dentro do escopo da função 'dentro', 
"""
def fora_1():
    a = 1

    def dentro_1():
        return a # 'a' é uma variável livre aqui
    return dentro_1

dentro = fora_1()
print("Valor de a:", dentro())  # Saída: 1




print("\n#########################################\n")
"""
locals()

A função 'locals()' retorna um dicionário representando a tabela de símbolos local.
Dentro de uma função, ela mostra as variáveis locais definidas naquele escopo.
"""

def fora_2(n):
    x = n

    def dentro_2():
        print("Locals dentro de 'dentro':", locals())
        return x # 'x' é uma variável livre aqui
    return dentro_2

a = fora_2(10)
print("Valor de a:", a())  # Saída: 10
b = fora_2(20)
print("Valor de b:", b())  # Saída: 20



print("\n#########################################\n")
"""
globals()

A função 'globals()' retorna um dicionário representando a tabela de símbolos global.
Dentro de uma função, ela mostra as variáveis globais definidas no escopo global.
"""

variavel_global = "Eu sou global"
def func_global():
    print("Globals dentro de 'func_global':", globals())
    return variavel_global  # 'variavel_global' é uma variável global aqui

print("Valor de variavel_global:", func_global())  # Saída: Eu sou global



print("\n#########################################\n")
"""
__code__.co_freevars

O atributo '__code__.co_freevars' de uma função retorna uma tupla com os nomes das
variáveis livres utilizadas dentro dessa função.
"""

def fora_3(mensagem):
    def dentro_3():
        print("Mensagem dentro de 'dentro_3':", mensagem)  # 'mensagem' é uma variável livre aqui
    return dentro_3

func = fora_3("Olá, Mundo!")
print("Variáveis livres em 'dentro_3':", func.__code__.co_freevars)  # Saída: ('mensagem',)
func()  # Saída: Olá, Mundo!



print("\n#########################################\n")
"""
Problema com variáveis livres

Quando uma variável livre é modificada na função interna, pode levar um UnboundLocalError.
"""

def concatenar(string_inicial):
    valor_final = string_inicial
    def adicionar_mais(valor_a_concatenar):
        valor_final += valor_a_concatenar # Modificando a variável livre
        return valor_final
    return adicionar_mais

c = concatenar("Olá, ")

try:
    print(c("Mundo!"))  # Tentando chamar a função interna
except UnboundLocalError as e:
    print("Erro ao tentar modificar a variável livre:", e)




print("\n#########################################\n")
"""
Para corrigir o problema anterior, podemos usar 'nonlocal' (ver o módulo '3_nonlocal.py')

Isso indica que a variável pertence ao escopo da função externa, permitindo sua modificação
e evitando o erro. O nonlocal transforma a variável livre em uma variável não local.
"""

def concatenar_corrigido(string_inicial):
    valor_final = string_inicial
    def adicionar_mais_corrigido(valor_a_concatenar):
        nonlocal valor_final  # Declarando que queremos usar a variável livre 'valor_final'
        valor_final += valor_a_concatenar
        return valor_final
    return adicionar_mais_corrigido

c_corrigido = concatenar_corrigido("Olá, ")
print("Concatenação feita:", c_corrigido("Mundo!"))  # Saída: Olá, Mundo
