def aritmetica(funcao):
    def soma(x, y):
        # funcao()
        print("Soma: ", x + y)
    return soma


@aritmetica  # Função pai. Decorada.
def mensagem():
    print("AAAAAAAA")


# nova_var = aritmetica(mensagem)
print("---------------")
# nova_var()

mensagem(20, 10)  # Veja que passei parâmetros para 'mensagem', sendo que 'mensagem' não recebe parâmetros.
# Isso acontece pq usando @ posso praticamente dizer que mensagem = soma. E assim consigo executar uma função dentro
# de outra usando outra função.
