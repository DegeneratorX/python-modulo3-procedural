"""
Pacotes (Packages) em Python

Pacotes são uma forma de estruturar módulos em diretórios hierárquicos. 
Eles permitem organizar o código em namespaces, facilitando a manutenção e 
reutilização.
"""


"""
Importando um módulo de um pacote usando import
"""
import pacote.modulo_2

print("Acessando variável do módulo_2:", pacote.modulo_2.variavel_modulo_2)
resultado = pacote.modulo_2.multiplica(3, 4)
print("Resultado da multiplicação usando função do módulo_2:", resultado)




print("\n################################################\n")
"""
Importando módulos de um pacote usando from ... import

Essa forma de improtação é mais concisa e utilizada para pacotes, e evita 
verbosidade ao acessar elementos do módulo.
"""

from pacote import modulo_2

print("Acessando variável do módulo_2 diretamente:", modulo_2.variavel_modulo_2)
resultado = modulo_2.multiplica(5, 6)
print("Resultado da multiplicação usando função do módulo_2:", resultado)





print("\n################################################\n")
"""
Importando elementos específicos de um módulo dentro de um pacote
"""

from pacote.modulo_2 import multiplica, variavel_modulo_2

print("Acessando variável do módulo_2 diretamente:", variavel_modulo_2)
resultado = multiplica(7, 8)
print("Resultado da multiplicação usando função importada diretamente:", resultado)