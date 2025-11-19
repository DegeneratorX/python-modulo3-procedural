"""
map() é uma função built-in que recebe uma função, um iterável e retorna um iterador.

map() tem a seguinte função: pegar um iterável (dict, listas etc etc.) e aplicar uma função sobre ela.
No caso do exemplo abaixo, irei pegar um iterável e aplicar uma função que captura esse iterável e multiplica todos os
valores nele por 2.

Existe uma forma de fazer isso com list comprehension, por sinal é bem mais fácil, porém quando importar dicts,
map() funcionará muito melhor que list comprehension.

Multiplicar por 2 com list comprehension ficará comentada, pois não é o foco principal do arquivo.
"""


from dados import lista  # Consigo importar dados de outro arquivo.

print(lista)  # Provando que a lista foi importada.
nova_lista = map(lambda x: x * 2, lista)  # Passo uma função que recebe um parâmetro e retorna ele *2.
print(list(nova_lista))


# O parâmetro x é um iterador que recebe o valor lista e itera sobre cada valor nele.
# Assim, ele retornará todos os valores possíveis dentro dessa lista *2.
# Por ser um iterador, ele não irá mostrar tudo de uma vez. Portanto, para mostrar, usa-se next() ou converte em list().

# Resumindo: map() pega uma função e aplica sobre um iterável, de forma completamente automática, retornando algo.

# nova_lista = [x * 2 for x in lista]
# Essa é outra forma de resolver. Mas com dicts já não funciona bem. Ai que entra o map().
