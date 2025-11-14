"""
Infelizmente não é tão simples copiar um dicionário pra outra variável,
pois no python as coisas funcionam de forma diferente. Ao copiar, as duas
variáveis apontam pro mesmo endereço de memória.

Exemplo:
v = dicionario_generico não é aconselhado, pois se mudar valores dentro de
'v', irá também mudar valores do dicionario_generico.

Existem formas melhores de copiar um dicionário pra uma nova variável.
Exemplos abaixo.

"""

d1 = {'chave1': 'a', 'chave2': 'b', 3: 'c', 'chave_lista': ['trynda', 'mere']}
v = d1  # "Cópia" de um dicionário pra uma variável nova.

v['chave1'] = 'Victor'

print(d1)
print(v)  # Perceba que os valores são IDÊNTICOS! Pois a atribuição na verdade apontam pro mesmo endereço.
print(v == d1)

#######################################################
print()
# Solução de baixo nível (cópia rasa): .copy()

v = d1.copy()
v['chave1'] = 'Victor - Agora vai!'
print(d1)
print(v)

# O problema dessa solução é que ao ter dicionários ou listas dentro de um dicionário,
# o valor não é alterado e continuará a acompanhar a variável original.
print()

v['chave_lista'][0] = 'Joao'  # Joao substitui Trynda. Índice 0 da lista.
print(d1)
print(v)  # Mesmo usando copy em v, alterou o d1 original!
