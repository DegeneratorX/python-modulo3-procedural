"""
copy() - cria uma cópia rasa (shallow copy) do dicionário. O motivo é que a atribuição direta cria uma referência à mesma lista na memória.
Modificar valores na variável que recebe a lista afetará a original. Tudo no final das contas é ponteiro.
Complexidade O(n), pois precisa copiar todos os elementos do dicionário para o novo dicionário.

Exemplo:
# Isso aqui não é aconselhado, pois se mudar valores dentro de 'v', irá também mudar valores do dicionario_generico.
v = dicionario_generico

Existem formas melhores de copiar um dicionário pra uma nova variável.
Exemplos abaixo.

"""

d1 = {'chave1': 'a', 
      'chave2': 'b', 
      3: 'c', 
      'chave_lista': ['trynda', 'mere']
}

v = d1  # Isso aqui NÃO COPIA!!

v['chave1'] = 'Victor'

print("Dicionário d1:", d1)
print("Variável 'v':", v)
print("Testando v == d1:", v == d1)  # Perceba que os valores são IDÊNTICOS! Pois a atribuição na verdade apontam pro mesmo endereço.


"""
Solução: copia rasa (shallow copy)
"""

v = d1.copy()
v['chave1'] = 'Victor - Agora vai!'
print("Dicionário d1:", d1)
print("Variável 'v':", v)

print("\n############################################\n")

"""
O problema dessa solução é que ao ter dicionários ou listas dentro de um dicionário,
o valor não é alterado e continuará a acompanhar a variável original.
"""

v['chave_lista'][0] = 'Joao'  # Joao substitui Trynda. Índice 0 da lista.
print("Dicionário d1:", d1)
print("Variável 'v':", v)  # Mesmo usando copy em v, alterou o d1 original!