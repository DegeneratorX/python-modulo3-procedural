"""
Função Decoradora e Decoradores

O conceito de decorar é:
- Adicionar
- Remover
- Restringir
- Alterar

Funções Decoradoras são funções que decoram (enfeitam) outras funções

Já os Decoradores são usados para fazer o interpretador usar as Funções Decoradoras
em outras funções.
"""

"""
Decorando uma função manualmente

Para decorar uma função manualmente, criamos uma função que recebe outra função como parâmetro
e retorna uma nova função que adiciona comportamento à função original.
"""

def criar_funcao_1(func):
    def interna_1():
        resultado = func() + ", Decorada!" # Nesse momento estou decorando a função passada como parâmetro
        return resultado
    return interna_1

def saudacao():
    return 'Olá'

nova_saudacao = criar_funcao_1(saudacao)  # Decorando a função manualmente
print(nova_saudacao())  # Saída: Olá, Decorada!





print("\n#########################################\n")
"""
Exemplo - Função Simples

Veja que a função abaixo inverte uma string. Mas se passarmos um número inteiro,
forçaremos erro, pois inteiros não suportam slicing. O erro ocorre na função
original, e isso pode ser um problema em alguns casos.
"""

def inverte_string_1(string):
    return string[::-1]

string_invertida_1 = inverte_string_1 ("Python")
print("Valor de 'string_invertida_1':", string_invertida_1)  # Output: nohtyP


print("\n--- Testando com número inteiro ---\n")
try: 
    numero_invertido_1 = inverte_string_1(12345) # TypeError
except TypeError as e:
    print("Erro:", e)



print("\n################################################\n")
"""
Solução do Exemplo acima com Decorador

Usando uma função decoradora, podemos modificar o comportamento da função original para
verificar o tipo do parâmetro antes de tentar inverter a string, e assim o erro que
forçaremos será tratado pela função decoradora.

O 'print(f"Nome dessa função aqui: {inverte_string_2.__name__}")' dentro da função 'inverte_string_2'
mostra que o nome da função original está preservado. Isso fará mais sentido no próximo módulo.
"""


# Essa é a função decoradora
def criar_funcao_2(func):

    # Essa é a função interna que adiciona comportamento à função original
    def interna_2(*args, **kwargs):
        print("Vou te decorar")

        for arg in args:
            is_string(arg)

        resultado = func(*args, **kwargs) + " Decorada!"
        print("O seu resultado foi:", resultado)
        print("Decoração finalizada")

        return resultado
    
    return interna_2


# Função para verificar se o parâmetro é uma string
def is_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError("Parâmetro deve ser uma string.")


# A função original que será decorada
def inverte_string_2(string):
    print(f"Nome dessa função aqui: {inverte_string_2.__name__}")
    return string[::-1]


inverte_string_nova_funcao = criar_funcao_2(inverte_string_2)
print(inverte_string_nova_funcao("Python"))  # Saída: nohtyP Decorada!


print("\n--- Testando com número inteiro ---\n")
try:
    print(inverte_string_nova_funcao(12345))  # TypeError
except TypeError as e:
    print("Erro:", e)

"""
Veja que o erro foi tratado pela função decoradora, antes de chamar a função original.
Ou seja, a função decoradora adicionou um comportamento extra à função original.

O problema é que decorar funções manualmente assim pode ser trabalhoso.
Além disso, a quantidade de código aumenta consideravelmente.

A solução do Python para isso são os Decoradores, que está no próximo módulo.
"""
