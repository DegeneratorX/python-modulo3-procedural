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


"""
Pacote 1

Mostrando que o diretório é um pacote apenas com o arquivo __init__.py vazio.
Essa é a forma padrão para sinalizar ao desenvolvedor que o diretório é um pacote.
"""
import pacote_1
print("Pacote 'modulo_pacote_1': ", pacote_1)





print("\n#########################################\n")
"""
Pacote 2

Mostrando que o diretório é um pacote com o arquivo __init__.py contendo
código que define variáveis e funções disponíveis diretamente a partir do pacote.

Isso "transforma" o pacote em um módulo, permitindo que seja possível acessar
diretamente essas variáveis e funções a partir do pacote.
"""
import pacote_2
print("Pacote 'modulo_pacote_2': ", pacote_2)
print("Variável do pacote 2 acessada diretamente: ", pacote_2.variavel_de_pacote_2)
print("Função dobra do pacote 2 acessada diretamente: ", pacote_2.dobra(10))






print("\n#########################################\n")
"""
Pacote 3

Mostrando que o diretório é um pacote com o arquivo __init__.py que importa
um módulo interno, servindo como intermediário para acessar o conteúdo do módulo
diretamente a partir do pacote.
"""
import pacote_3
print("Pacote 'modulo_pacote_3': ", pacote_3)
print("Fatorial de 5 acessado diretamente: ", pacote_3.fatorial(5))
print("Fibonacci de 10 acessado diretamente: ", pacote_3.fibonacci(10))
print("Variável do módulo 3 acessada diretamente: ", pacote_3.variavel_de_modulo)