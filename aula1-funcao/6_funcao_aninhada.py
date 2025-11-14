"""
É possível definir uma função dentro de outra função. Isso é chamado de função aninhada.
Uma função aninhada pode acessar variáveis e parâmetros da função externa.
"""

def funcao_externa():
    x = 10  # Variável da função externa

    def funcao_interna():
        y = 2  # Variável da função interna 
        print(f'Valor de x dentro da função interna: {x}')  # Acessando variável da função externa
        print(f'Valor de y dentro da função interna: {y}')  # Acessando variável da função interna

    funcao_interna()  # Chamando a função interna
    print(f'Valor de x dentro da função externa: {x}')  # Acessando variável da função externa


funcao_externa() # Chamando a função externa (execução padrão em quase todas as linguagens de programação)

############################################################################################################################################
# Observações importantíssimas:
#
# - y não pode ser acessada fora da 'função_interna', pois seu escopo é limitado à 'função_interna'.
# - x pode ser acessada dentro da 'função_interna', pois funções aninhadas podem acessar variáveis da 'função_externa'.
# - x não pode ser acessada fora da 'função_externa', pois seu escopo é limitado à 'função_externa'.
# - chamar 'funcao_interna()' fora de 'funcao_externa' resultará em erro, pois 'funcao_interna()' não está definida no escopo global. 
############################################################################################################################################

"""
Para resolver o problema de acessar valores de funções externas, podemos retornar a função interna.
"""

def funcao_externa_retorna():
    x = 20

    def funcao_interna_retorna():
        print(f'Valor de x dentro da função interna que é retornada: {x}')

    return funcao_interna_retorna  # Retornando a função interna sem os parênteses  

minha_funcao_interna = funcao_externa_retorna()  # Atribuindo a função retornada a uma variável
minha_funcao_interna()  # Chamando a função interna através da variável

# Observação: Ao retornar a função interna, ela mantém o acesso às variáveis da função externa, mesmo após a execução da função externa ter terminado.





print("\n################################################\n")

"""
nonlocal - palavra-chave

Para acessar variáveis de funções externas em funções internas, podemos usar a palavra-chave 'nonlocal'. 
Isso permite modificar variáveis da função externa dentro da função interna.
Sem nonlocal, a variável seria tratada como uma nova variável local dentro da função interna,
e só poderia ser lida, não modificada.
"""

def funcao_externa_nonlocal():
    contador = 0  # Variável da função externa

    def funcao_interna_nonlocal():
        nonlocal contador  # Declarando que queremos usar a variável 'contador' da função externa
        contador += 1  # Modificando a variável da função externa
        print(f'Contador dentro da função interna: {contador}')

    funcao_interna_nonlocal()  # Chamando a função interna
    funcao_interna_nonlocal()  # Chamando novamente para ver a modificação
    print(f'Contador dentro da função externa após chamadas internas: {contador}')  # Acessando a variável modificada

funcao_externa_nonlocal()  # Chamando a função externa




print("\n################################################\n")

"""
global - palavra-chave

A palavra-chave 'global' permite que uma função interna acesse e modifique uma variável global.
"""

variavel_global = 0  # Variável global
def funcao_externa_exemplo_com_global():
    global variavel_global  # Declarando que queremos usar a variável global
    variavel_global += 10  # Modificando a variável global

    def funcao_interna_exemplo_com_global():
        global variavel_global  # Declarando que queremos usar a variável global
        variavel_global += 13
        print(f'Valor da variável global dentro da função interna : {variavel_global}')

    print(f'Valor da variável global dentro da função externa antes da chamada interna: {variavel_global}')
    funcao_interna_exemplo_com_global()  # Chamando a função interna
    print(f'Valor da variável global dentro da função externa após chamada interna: {variavel_global}')  # Acessando a variável global modificada

funcao_externa_exemplo_com_global()  # Chamando a função externa
print(f'Valor da variável global fora de todas as funções: {variavel_global}')