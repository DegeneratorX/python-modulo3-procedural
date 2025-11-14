"""
Função - def em python
Função serve pra evitar alterações massivas de linhas de código, além de reaproveitamento de código.
Uma função pode receber ou não parâmetros, e pode ou não retornar valores.
"""


def funcao(msg, nome):
    print(msg, nome)


funcao("Olá!", "Victor")  # Se eu chamar 1 ou 0 parâmetros, dará erro de exceção.
funcao("Eae", "Martins")
funcao("Blz", "João")
funcao("Show", "Maria")

#######################################
print()

"""
Parâmetros default - São parâmetros que já vêm com um valor pré-definido na função.
Se na chamada da função eu não passar nenhum valor para o parâmetro, ele usará o valor default.
Mas se eu passar um valor, ele substituirá o valor default.
"""
def saudacao(msg = 'Olá', nome = 'Usuário'):  # Definidos default.
    print(msg, nome)


saudacao()  # Nos parâmetros, se estiver definido algo, será o default. Então é possível executar dessa forma sem erro.
saudacao('Oi', 'GGGGGG')  # Mas se um parâmetro for passado pra função, automaticamente substitui o default.
saudacao('Hello', 'Eoqq?')
saudacao(nome='Zezinho')  # Mas se eu passar especificamente o parâmetro que será passado, ele substituirá o parâmetro.
saudacao(nome='Zezão', msg='Hi')
