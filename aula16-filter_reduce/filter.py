"""
filter() filtra dados.
Parâmetros extremamente semelhantes da função map(). Retorna um iterador.
IMPORTANTE: Rever a aula de map() é essencial para entender melhor como funciona filter() e reduce().
"""

from dados import produtos, lista
###############
# Jeito tradicional usando list comprehension:
# nova_lista = [x for x in lista if x > 5]
###############

nova_lista = filter(lambda x: x > 5, lista)  # passo a função + o iterável.
print(list(nova_lista))

novo_produto = filter(lambda p: p['preco'] > 50, produtos)  # Produtos com preço maior que 50 reais.
for produto in novo_produto:  # Mostrando todos esses produtos maiores que 50 reais.
    print(produto)

###########################
print()
print('#'*40)
print()


def filtra(product):
    if product['preco'] > 50:
        return True
    else:
        return False


novo_produto2 = filter(filtra, produtos)  # Funciona da mesma forma, só um pouco mais complexo.

for produto in novo_produto2:
    print(produto)

# Com isso também é possível fazer com pessoas para saber menores ou maiores de idade.
