from dados import pessoas

for pessoa in pessoas:
    print(pessoa)  # Comprovando que o dict foi importado

####################################
print()
print('#'*40)
print()

nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)  # Imprimindo apenas os nomes.

####################################
print()
print('#'*40)
print()
# Agora vou fazer um exemplo de adição de uma chave nova ao dicionário + aumento de idade


def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)  # Aumento em 20% as idades
    return p


idade = map(aumenta_idade, pessoas)  # Passo a função aumenta_idade, e ela atuará em todo o dicionário.

for pessoa in idade:
    print(pessoa)
