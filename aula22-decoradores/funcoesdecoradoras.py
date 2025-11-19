"""
Funções decoradoras recebem uma função como parâmetro e decoram/modificam
ela retornando uma nova a ser usada no lugar.

OBS: Quando é apenas func, sem (), a função não estará sendo executada.
func() automaticamente executa ela.
"""


def decorar(funcao):

    # Geralmente, ao decorar uma função, deseja-se substituí-la por outra.
    # E esta abaixo irá substituir a recebida como parâmetro acima
    def funcao_decorada():
        print('############')
        funcao()
        print('############')

    return funcao_decorada


def printar():
    for i in range(3):
        print(i)


nova_printar = decorar(printar)

nova_printar()

# Saída:
# ############
# 0
# 1
# 2
# ############
#
# Ou seja, fizemos uma decoração/modificação na função printar().
# Ao colocar o @decorador em cima de uma função X, o que o
# interpretador do Python faz é PRATICAMENTE printar = funcao_decorada. Próximo arquivo mostra isso.
