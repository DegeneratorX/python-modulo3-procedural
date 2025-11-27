"""
Decorador em Python

Um decorador é um syntax sugar em Python que permite modificar o comportamento de uma função
ou método sem alterar seu código fonte diretamente. Ele é aplicado usando o símbolo "@" acima
da definição da função que se deseja decorar.

Decoradores são usados para fazer o Python usar as funções decoradoras em outras
funções.
"""


"""
Solução do Exemplo do módulo '1_funcao_decoradora.py' com Decorador

Perceba que é tudo automático, não precisamos mais chamar a função decoradora manualmente.
Além disso, o código fica mais limpo e fácil de entender.

Esse código é equivalente ao do módulo '1_funcao_decoradora.py', mas usando a 
sintaxe de decoradores do Python. O Python entende que a função 'inverte_string_2'
deve ser passada para a função decoradora 'criar_funcao_2' automaticamente.

E note que o nome da função original é modificado temporariamente para o nome da função
interna da função decoradora. Mas isso não afeta o funcionamento da função decorada.
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
@criar_funcao_2
def inverte_string_2(string):
    print(f"Nome dessa função aqui: {inverte_string_2.__name__}")
    return string[::-1]
    

string_invertida = inverte_string_2("Python")
print(string_invertida)  # Saída: nohtyP Decorada!


print("\n--- Testando com número inteiro ---\n")
try:
    print(inverte_string_2(12345))  # TypeError
except TypeError as e:
    print("Erro:", e)



