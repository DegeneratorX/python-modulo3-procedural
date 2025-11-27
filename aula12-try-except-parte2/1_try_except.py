"""
Na aula 12 foi apresentado o bloco try except básico.

A ideia agora é mostrar mais algumas possibilidades de uso do try except, como:
- Múltiplas exceções;
- Capturar o erro específico;
- Else;
- Finally.
"""


"""
Try Except Básico
"""
try:
    a = 18
    b = 0
    print("Até aqui tudo bem...")
    c = a / b
    print("Isso não será impresso, pois houve um erro na linha anterior.")
except:
    print("Dividiu por zero.")

print("Continua...")




print("\n#######################################\n")
"""
Try Except por boa prática, sempre capturar o erro específico

O motivo é que, ao capturar o erro específico, evitamos capturar erros
inesperados que podem ocorrer em outras partes do código dentro do bloco try.
Assim, podemos tratar cada tipo de erro de maneira adequada e fornecer
mensagens de erro mais informativas.
"""

try:
    a = 18
    b = 0
    print("Até aqui tudo bem...")
    c = a / b
    print("Isso não será impresso, pois houve um erro na linha anterior.")
except ZeroDivisionError:
    print("Dividiu por zero.")
print("Continua...")



print("\n#######################################\n")
"""
Try Except com Múltiplas Exceções

Às vezes, um bloco de código pode gerar diferentes tipos de exceções. Nesses
casos, podemos usar múltiplas cláusulas except para capturar e tratar cada
tipo de exceção de maneira adequada.

Uma exceção é uma classe que herda da classe base Exception. Podemos capturar
várias exceções em um único bloco try usando múltiplas cláusulas except.
"""

try:
    a = 10
    b = int(input("Denominador: "))
    c = a / b # Isso gera um ZeroDivisionError se b for zero.
    print(a[100]) # Isso gera um IndexError, pois a é um inteiro e não uma lista.
except ZeroDivisionError:
    print("Dividiu por zero.")
except ValueError:
    print("Valor incorreto.")
except (TypeError, IndexError): # Captura múltiplas exceções em uma única cláusula except.
    print("Tipo ou índice incorreto.")

# Captura qualquer outra exceção que não foi tratada acima.
# O 'e' captura o objeto da exceção para que possamos imprimir ou logar a 
# mensagem de erro.
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
    print("Nome da classe do erro:", e.__class__.__name__) # Mostra o nome da classe do erro.

print("Continua...")