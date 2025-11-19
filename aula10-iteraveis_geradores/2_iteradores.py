lista = [0, 1, 2, 3, 4, 5]

lista = iter(lista)  # Conversão de um iterável para um iterador.

print(hasattr(lista, '__next__'))  # Check pra ver se agora é um iterador através do '__next__'.
# Retornará True dessa vez.

# Agora posso usar a função next() em 'lista', já que agora 'list' é um iterador.
# Sem a conversão para um iterador usando iter(), as linhas abaixo dariam erro.
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

# Resumo: Um iterável é um obj que você pode iterar sobre ele, mas ele não vai dar um valor de cada vez.
#         Um iterador sempre vai te dar um valor de cada vez sempre que preciso.
#         Um iterável não necessariamente é um iterador.
#         Mas todo iterador é um iterável.
