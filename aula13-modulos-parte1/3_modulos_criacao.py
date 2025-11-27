"""
Criando módulos em Python

Módulos em Python são arquivos que contêm definições e implementações de funções,
classes e variáveis que podem ser reutilizados em outros programas. Criar módulos ajuda
a organizar o código, promover a reutilização e facilitar a manutenção.
"""

import modulo_1

print("Este é o módulo '__main__.py' sendo executado: ", __name__)
print(modulo_1.variavel_modulo)

from modulo_1 import variavel_modulo
print(variavel_modulo)

from modulo_1 import soma
resultado = soma(5, 7)
print("Resultado da soma usando a função do módulo:", resultado)