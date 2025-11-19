"""
json = JavaScript Object Notation
"""

import json

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': '25',
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    },
}

d1_json = json.dumps(d1, indent=True)  # Conversão para o tipo json. indent ajusta o dicionário pra ficar organizado.
# Sem indent (indentação), tudo ficaria na mesma linha.

print(d1_json)  # Igual dicionário, mas agora pode ser lido por vários programas através da extensão .json.

with open('abc.json', 'w+') as file:
    file.write(d1_json)

