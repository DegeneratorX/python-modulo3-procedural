"""
Módulos padrão do Python:
Módulos são arquivos .py (que contém código python) e que servem para expandir
as funcionalidades padrão da linguagem.
Todos os módulos: https://docs.python.org/3/py-modindex.html
"""
from sys import platform as os  # Importando a função platform do módulo sys. Renomeio como 'os', e posso
#                                 usar como 'os' a qualquer momento.
import random  # Biblioteca random. Não usei "from", então precisarei passar random.randint().


print(os)  # Imprime o atual sistema operacional utilizado.

for i in range(10):
    print(random.randint(0, 10))  # Imprime 10 números aleatórios de 0 a 10.

