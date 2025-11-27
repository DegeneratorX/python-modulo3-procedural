"""
Sets (conjuntos) em Python

Conjuntos são os mesmos que conjuntos na matemática. Representados pelo diagrama
de Venn, sets são mutáveis, mas aceitam apenas tipos imutáveis como elementos.
Além disso, não possuem elementos duplicados e não possuem ordem (não são indexados).
Apesar disso, podemos iterar sobre os elementos do set.

- add (adiciona), update (atualiza), clear, discard
- union  | (une)
- intersection & (todos os elementos presentes nos dois sets)
- difference - (elementos apenas no set da esquerda)
- symetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

Funciona parecido com listas e tuplas. A diferença é que
se usa chaves, igual dicionário.

NÃO CONFUNDIR. Dicionários são pares. Sets são singulares,
igual listas e tuplas.
"""

"""
Criando sets

Para criar um set, usamos chaves {} com elementos imutáveis ou a função set().
"""

s1 = {1, 2, 3, 4, 5} # Criação de um set com elementos.
print("Conjunto s1:", s1)

# ATENÇÃO: Para criar um set vazio, devemos usar a função set().
# Usar {} cria um dicionário vazio.
eh_um_dicio_nao_um_set = {}  # Dicionário vazio.
print("Tipo de dicio:", type(eh_um_dicio_nao_um_set))

s2 = set()  # Formato correto para criar um set vazio.
print("Tipo de s2:", type(s2))

"""
Adicionando e removendo elementos

Usamos o método .add() para adicionar elementos 
e o método .discard() para remover elementos.
"""

s2.add(1)  # Adiciona o elemento no set.
s2.add(2)
s2.add(3)
s2.discard(2)  # Remove o elemento do set. 
elem = s2.pop()  # Remove um elemento aleatório do set.

print("Conjunto s2:", s2)
print("Elemento removido com pop():", elem)

print("\n#############################################\n")
"""
Atualizando elementos

Usamos o método .update() para adicionar múltiplos elementos a um set.

A diferença entre .add() e .update() é que o .add() adiciona um único
elemento ao set, enquanto o .update() pode adicionar múltiplos elementos.
Pode ser passado um iterável (como listas, tuplas, strings, outros sets) 
para o .update(), e ele irá iterar sobre esse iterável, adicionando cada
elemento individualmente ao set.
"""

s2.update('Python')  # Update itera sobre cada letra da palavra. Essa é a principal diferença com o .add().
print("Conjunto s2 após update com string:", s2)
s2.update([1,2,3], {3,4,5})  # O set não repete elementos. Aqui ele tá adicionando uma lista e outro set (subset).
print("Conjunto s2 após update com lista e set:", s2)  # No final, concatenou tudo e evitou repetiçoes.

"""
Remover repetições de um iterável

Existem várias formas de remover repetições de uma lista, tupla ou string. A mais simples
é converter o iterável para set e depois converter de volta para o tipo original
"""

l1 = [1,1,2,2,2,3,4,5,7,7,'Victor', 'Victor']

tirar_repeticoes = set(l1)  # Conversão para Set. Uma utilidade simples pra eliminar repetições de uma lista ou tupla.
l1 = list(tirar_repeticoes)  # Conversão de volta para lista.
print("Lista l1 após remover repetições:", l1)

print("\n#############################################\n")

"""
Operações com conjuntos

- União: É a junção de todos os elementos dos dois sets.
- Interseção: São todos os elementos presentes nos dois sets ao mesmo tempo.
- Diferença: São os elementos presentes apenas no set da esquerda.
- Diferença simétrica: São os elementos que estão nos dois sets, mas não em ambos.
"""
s3 = {2,3,4,7}
s4 = {1,2,3,4,5,6}
s5 = s3 | s4  # União dos conjuntos!

print("Conjunto s5 após união entre s3 e s4:",s5)

s6 = s3 & s4  # Interseção dos conjuntos!
print("Conjunto s6 após interseção entre s3 e s4:", s6)

s7 = s4 - s3  # Diferença entre conjuntos!
s8 = s3 - s4  # A ordem importa.
print("Conjunto s7 após diferença entre s4 e s3:", s7)
print("Conjunto s8 após diferença entre s3 e s4:", s8)

s9 = s3 ^ s4  # Diferença simétrica entre conjuntos!
print("Conjunto s9 após diferença simétrica entre s3 e s4:", s9)

print("\n#############################################\n")
"""
Iterando sobre sets

Podemos iterar sobre os elementos de um set usando loops.
- for
- while
- in, not in
"""

s10 = {'Victor', 1, 2, 3, 4, 5}
for elemento in s10:
    print("Elemento do set s10:", elemento) # Sempre em ordem aleatória, pois sets não são indexados.

print("Verificando se o elemento 'Victor' está no set s10:", 'Victor' in s10)  # Verifica se o elemento está no set.
print("Verificando se o elemento 10 não está no set s10:", 10 not in s10)  # Verifica se o elemento não está no set.

while s10:
    elemento = s10.pop()  # Remove e retorna um elemento aleatório do set.
    print("Removendo elemento do set s10:", elemento)