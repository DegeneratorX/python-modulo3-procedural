from dados import produtos  # Agora importo produtos.

for produto in produtos:  # Provando que produtos foram importados
    print(produto)

############################################
print()
print('#'*40)
print()

precos = map(lambda p: p['preco'], produtos)  # A função lambda recebe o dict e retorna apenas as chaves 'preco'.

for preco in precos:
    print(preco)  # Imprimirá somente os valores dos índices 'preco'.

############################################
print()
print('#'*40)
print()

# Para aumentar o preço dos produtos em 5%, já não convém usar lambda, pois a soma é mais complexa.


def aumenta_preco(p):  # Ao invés do lambda, criaremos uma função normal.
    p['preco'] = round(p['preco'] * 1.05, 2)  # arredondamento para 2 casas decimais
    return p  # Retornando p['preco'] retornaria apenas os novos precos, sem o dicionario todo.


novos_precos = map(aumenta_preco, produtos)  # Passo a função e o iterável dicionário 'produtos'.

for precos in novos_precos:
    print(precos)
