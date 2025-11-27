"""
Higher Order Functions

Funções de ordem superior são funções que podem receber outras funções como argumentos ou retornar funções como resultado.
Elas são úteis para criar abstrações, manipular comportamentos e implementar padrões de design funcionais.
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa_funcao(funcao, *args):
    print(f'Conteúdo de args em executa_funcao: {args}')
    return funcao(*args)

print(executa_funcao(saudacao, 'Olá', 'Maria'))  # Exibirá: Olá, Maria!
print(executa_funcao(saudacao, 'Bom dia', 'João'))  # Exibirá: Bom dia, João!