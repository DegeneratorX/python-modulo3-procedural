"""
__init__.py em Python

O arquivo __init__.py é um componente especial em Python que indica que o 
diretório onde ele está localizado deve ser tratado como um pacote. Ele pode 
estar vazio ou conter código de inicialização para o pacote.

A não utilização de __init__.py em versões mais recentes do Python (3.3 e posteriores)
ainda permite que o diretório seja reconhecido como um pacote, mas a presença do
arquivo pode ser útil para compatibilidade com versões mais antigas do Python
e para definir o comportamento do pacote, além de ser uma prática comum em muitos projetos
para sinalizar claramente que o diretório é um pacote.

Quando __init__.py contém código, esse código é executado no momento em que o pacote é importado,
permitindo configurar variáveis, importar submódulos ou definir funções e classes
que estarão disponíveis quando o pacote for utilizado.

Esse arquivo meio que engana o interpretador Python para reconhecer o diretório como um
módulo propriamente, pois escrevendo em __init__.py, você pode chamar variáveis
e funções diretamente do pacote, sem precisar importar submódulos específicos.
"""

# TODO