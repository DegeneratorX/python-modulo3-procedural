"""
Módulos em Python (import, from, as, *)

Módulos são arquivos .py que possuem código Python e servem para organizar e reutilizar
códigos em diferentes programas. Podemos criar nossos próprios módulos ou usar módulos
padrão do Python (built-in) ou ainda instalar módulos de terceiros.
"""

"""
Importação Inteira (import module_name)

Podemos importar um módulo inteiro usando a palavra-chave import seguida do nome do módulo.
Ao fazer isso, precisamos usar o nome do módulo como prefixo para acessar suas funções,
variáveis ou classes.

- Vantagens: Vocẽ tem o namespace completo do módulo, evitando conflitos de nomes.
- Desvantagens: Nomes grandes podem ser verbosos ao usar várias funções do módulo.
"""

print("import math")
import math  # Importa o módulo math inteiro.
pi = 3.14159
print("Raiz quadrada de 16 é:", math.sqrt(16))  # Usando a função sqrt do módulo math.
print("Valor de pi é:", math.pi)  # Usando a constante pi do módulo math.
print("Valor de pi personalizado é:", pi)  # Usando a variável pi definida no código. Não conflita com math.pi.



print("\n#############################################\n")
"""
Importação Específica (from module_name import object_1, object_2, ...)

Também podemos importar partes específicas de um módulo usando a palavra-chave from seguida
do nome do módulo e a palavra-chave import seguida do nome da função, variável ou classe.
Dessa forma, podemos usar diretamente o nome da função, variável ou classe sem o prefixo
do módulo.

- Vantagens: Nomes mais curtos e código mais limpo.
- Desvantagens: Sem o namespace completo do módulo, o que pode levar a conflitos
 de nomes.
"""

print("from math import sqrt, pi")
from math import sqrt, pi  # Importa apenas a função sqrt e a constante pi do módulo math.

print("Raiz quadrada de 25 é:", sqrt(25))  # Usando a função sqrt diretamente.
print("Valor de pi é:", pi)  # Usando a constante pi diretamente.
pi = 3.14159  # Agora 'pi' é uma variável no código.
print("Valor de pi personalizado é:", pi)  # Usando a variável pi definida no código.



print("\n#############################################\n")
"""
Importação com Alias (import module_name as alias / from module_name import object as alias)

Podemos renomear módulos ou suas partes importadas usando a palavra-chave as. Isso é útil para evitar conflitos de nomes
ou para tornar o código mais legível. Porém, o recomendado é mudar o nome da variável do desenvolvedor,
e não o nome do módulo importado, pois conhecemos os módulos padrões da linguagem.

- Vantagens: Você pode reservar nomes para o seu código.
- Desvantagens: Pode ficar fora do padrão da linguagem se usado em excesso.
"""
print("import math as m")
import math as m  # Importa o módulo math e o renomeia como 'm'.

math = "Isso é uma string, não o módulo math."  # Agora 'math' é uma string no código.
print("Raiz quadrada de 36 é:", m.sqrt(36))  # Usando a função sqrt do módulo math renomeado.
print("Valor de pi é:", m.pi)  # Usando a constante pi do módulo math renomeado.
print("Valor da variável math:", math)  # Usando a variável math definida no código


print("from math import factorial as f")
from math import factorial as f  # Importa a função factorial e a renomeia como 'f'.
factorial = "Outra string, não a função factorial."  # Agora 'factorial' é uma string no código.
print("Fatorial de 5 é:", f(5))  # Usando a função factorial renomeada.
print("Valor da variável factorial:", factorial)  # Usando a variável factorial definida no código.


print("\n#############################################\n")
"""
Importação de Tudo (from module_name import *)

Podemos importar todas as funções, variáveis e classes de um módulo usando a sintaxe 
'from module_name import *'. No entanto, essa prática não é recomendada, pois pode 
levar a conflitos de nomes e dificultar a leitura do código.

- Vantagens: Importa tudo de um módulo.
- Desvantagens: Importa tudo de um módulo.  
"""

print("from math import *")
from math import *  # Importa tudo do módulo math.

print("Raiz quadrada de 49 é:", sqrt(49))  # Usando a função sqrt diretamente.
print("Valor de pi é:", pi)  # Usando a constante pi diretamente.
print("Fatorial de 6 é:", factorial(6))  # Usando a função factorial diretamente.

# Note que não há prefixo do módulo, mas isso pode causar conflitos se houver
# outras funções ou variáveis com os mesmos nomes no código.


print("\n#############################################\n")

"""
Qual método de importação usar?

- Use 'import module_name' quando quiser o namespace completo do módulo.
- Use 'from module_name import object' quando quiser apenas partes específicas do módulo.
- Use 'import module_name as alias' ou 'from module_name import object as alias' para renomear módulos ou partes importadas.
- Evite 'from module_name import *' para manter o código claro e evitar conflitos de nomes.

No geral, escolha o método que melhor se adapta às suas necessidades e ao estilo do seu código.

- No mercado se utiliza mais o 'import module_name' e o 'from module_name import object'.
- Para aprendizado e pesquisa, o 'from module_name import *' pode ser útil e rápido, mas evite em produção.
- O Alias ('as') é usado conforme a necessidade do desenvolvedor para evitar conflitos, 
ou pode ser utilizado como convenção da comunidade de desenvolvimento. Por exemplo, 
'import numpy as np' ou 'import pandas as pd' são amplamente utilizados na comunidade 
de ciência de dados.
"""