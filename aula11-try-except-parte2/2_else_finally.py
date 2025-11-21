"""
Else e Finally no Try Except

Além do bloco try e except, o Python também oferece as cláusulas else e finally
para tratamento de exceções.

- else: Executado quando o bloco try não gera nenhuma exceção.
- finally: Sempre executado, independentemente de uma exceção ter ocorrido ou não.

# Sobre o Finally:

A cláusula finally parece redundante, mas é muito útil para liberar recursos,
como fechar arquivos ou conexões de rede, garantindo que essas ações sejam
executadas mesmo que ocorra um erro, ou quando tem um return ou break no bloco
try ou except.

Sim, se você colocar o mesmo código após o bloco try except, ele também será 
executado, mas o finally deixa claro que aquele código é para "limpeza" ou 
"finalização", e por ele ser sempre executado, ele permite que seja executado 
mesmo se houver um return (function) ou break (loop) no bloco try ou except.

Exemplo: se eu crio uma função que abre um arquivo, e dentro do try 
eu faço um return com o conteúdo do arquivo, o finally vai garantir que o
arquivo seja fechado antes da função retornar o valor.
"""


def abrir_arquivo_erro_proposital():
    try:
        print("Abrindo arquivo...")
        arquivo = "arquivo.txt"  # Simulando a abertura de um arquivo.
        arquivo/2  # Isso gera um erro propositalmente.
        return arquivo
    except Exception as e:
        print("Erro ao abrir o arquivo:", e)
    finally:
        print("Fechando o arquivo...")


conteudo = abrir_arquivo_erro_proposital()


def abrir_arquivo_sucesso():
    try:
        print("Abrindo arquivo...")
        arquivo = "arquivo.txt"  # Simulando a abertura de um arquivo.
        return arquivo  # Mesmo com o return, o finally será executado.
    except Exception as e:
        print("Erro ao abrir o arquivo:", e)
    finally:
        print("Fechando o arquivo...")


conteudo = abrir_arquivo_sucesso()


print("\n#######################################\n")
"""
Else no Try Except

A cláusula else é executada quando o bloco try não gera nenhuma exceção.
É útil para código que deve ser executado apenas quando não há erros,
separando-o do código que pode gerar exceções. Pouco utilizado.
"""

print("Sem erro:")

try:
    a = 10
    b = 2
    c = a / b  # Isso não gera erro.
except ZeroDivisionError:
    print("Dividiu por zero.")
else:
    print("Não houve erro. O resultado é:", c)

print("Agora com erro, else não será executado:")

try:
    a = 10
    b = 0
    c = a / b  # Isso gera um ZeroDivisionError.
except ZeroDivisionError:
    print("Dividiu por zero.")
else:
    print("Não houve erro. O resultado é:", c)
