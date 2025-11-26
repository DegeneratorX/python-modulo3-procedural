"""
Entendendo a variável sys.path

A variável sys.path é uma lista em Python que contém os diretórios onde o interpretador 
procura por módulos e pacotes quando você tenta importá-los.

O primeiro múdulo executado se chama '__main__.py'. O interpretador conhece a pasta 
onde o '__main__.py' está, as pastas irmãs dele e as pastas abaixo dele. Ele não conhece pastas acima ou
em outro lugar do computador, a menos que você adicione esses caminhos manualmente
à variável sys.path.
"""

import sys

print("Esse módulo se chama:", __name__)


print("Caminhos onde o interpretador procura por módulos:")
print(*sys.path, sep="\n")

try:
    sys.path.append('/caminho/inexistente')
    print("\nCaminho adicionado com sucesso.")
except ModuleNotFoundError as e:
    print("Erro ao adicionar caminho:", e)


print("\nCaminhos atualizados onde o interpretador procura por módulos:")
print(*sys.path, sep="\n")

"""
Agora você pode adicionar import de módulos que estejam nesse novo caminho 
adicionado.

O VSCode acusa erro, mas se você criar o arquivo nesse caminho, o Python
conseguirá importar normalmente.
"""