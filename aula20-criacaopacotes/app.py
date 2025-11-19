"""
#########################
import vendas.calc_preco
    No código se usaria: vendas.calc_preco.aumento()
#########################
from vendas import calc_preco
    No código se usaria: calc_preco.aumento()
#########################
"""
from vendas.calc_preco import aumento, reducao  # Versão mais simples ainda.
import vendas.formata.preco

valor = 49.90
preco_com_aumento = aumento(valor=valor, porcentagem=15, formata=True)
print(preco_com_aumento)

preco_com_reducao = reducao(valor=valor, porcentagem=15, formata=True)
print(preco_com_reducao)

print(vendas.formata.preco.real(50))
