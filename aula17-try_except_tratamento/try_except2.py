"""
Try: Except: usando Else e Finally
"""
try:
    a = 1/0
except ZeroDivisionError as erro:
    print('Divisão por 0? Ta maluco? Detalhes do erro: ', erro)
finally:  # Finally é executado independente se o erro no try foi tratado ou não.
    print('Cuidado da próxima vez!')
    a = 'Valor desconhecido'  # Defino um valor para 'a', pois o try desconsiderou a declaração de valor 1/0. É como se
    #                           ela não tivesse existido.

print(a)  # Sem a = None, daria um erro aqui, pois é como se 'a' não tivesse sido declarado em 'try:'.

#############################
print()

try:
    b = {}
    print(b)
except Exception as erro:
    print('Isso aqui não será executado.')
else:  # Else é executado apenas se o Try funcionou normalmente.
    print('Isso aqui será executado.')
