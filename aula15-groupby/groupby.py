"""
groupby - serve pra agrupar valores de acordo com alguma chave ou índice escolhido.
Por ser um iterador, age com iteráveis apenas (string, listas, tuplas, dicts...)

Ex: Grupo A: 1,2,3,4 / Grupo B: 5,6,7,8 / Grupo C: 9, 10 etc.

IMPORTANTE: É necessário primeiro que o iterável esteja ordenado (.sort()) conforme a chave escolhida.
Usar groupby com iteráveis com a chave desejada não ordenada pode trazer resultados indesejáveis.
"""

from itertools import groupby, tee
from copy import deepcopy

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'Anderson', 'nota': 'B'},
]

chave = lambda item: item['nota']  # Criando uma função que retorne o índice (chave) que eu quero ordenar.

alunos.sort(key=chave)  # Uso .sort() com key=chave, pois o python não saberia o que ordenar exatamente sem essa key.
#                         Por isso inclusive que foi criada a função.
alunos_agrupados = groupby(alunos, chave)  # Agrupo finalmente. Por ser um iterador, por si só isso não retorna nada.
# Como passei o parâmetro 'chave', ele agrupará os valores conforme as notas.

alunos_agrupados_print = deepcopy(alunos_agrupados)  # Faço uma cópia profunda, pois irei iterar sobre essa cópia apenas
# pra printar ela, afinal print() também itera sobre um valor. Print iria esvaziar os valores e não poderia continuar na
# próxima iteração com um for, por exemplo (não iria mostrar nada).

print(type(alunos_agrupados_print))
print(list(alunos_agrupados_print))  # Como se pode ver, foram agrupados em tuplas com A, B, C e D como chaves.
# É basicamente isso que groupby() faz.
print()
'''
# Sem tee (com list)
for agrupamento, valores_agrupados in alunos_agrupados:
  valores = list(valores_agrupados)
  print(f'Agrupamento: {agrupamento}')
  for aluno in valores:
    print(f'\t{aluno}')
  quantidade = len(valores)
  print(f'\t{quantidade} alunos tiraram nota {agrupamento}')
'''

# Com tee
for agrupamento, valores_agrupados in alunos_agrupados:  # Desempacotamento.
    v1, v2 = tee(valores_agrupados)  # Como vou iterar 2 vezes no mesmo valor, iria esgotar o iterável. .tee() resolve.
    # Tee basicamente copia um iterador para dois novos idênticos. Como estou copiando um iterável para 2
    # em simultâneo, tee() se torna uma opção melhor que deepcopy().

    print(f'Agrupamento: {agrupamento}')

    for aluno in v1:  # Copiando para dois valores, assim posso iterar...
        print(f'\t{aluno}')

    quantidade = len(
        list(v2))  # ...e depois mostrar o tamanho, afinal len() itera também, e mostraria vazio sem o .tee()
    print(f'\t{quantidade} alunos tiraram nota {agrupamento}')

# Resultado: agrupamento de vários dicionários baseados na chave escolhida, as notas.
