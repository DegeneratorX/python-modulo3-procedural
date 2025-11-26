"""
Obs: arquivos .json não tem como acessar chaves.
"""

import json

with open('abc.json', 'r') as file:  # Abro o arquivo .json
    d1_json = file.read()  # Leio o arquivo e guardo na memória
    print(d1_json)

    d1_json = json.loads(d1_json)  # Conversão de volta para um dicionário.
    print(d1_json)  # Provando que voltou pra dicionário

    for k, v in d1_json.items():  # Mostrando os itens no dicionário
        print(k)
        for k1, v1 in v.items():
            print(k1, v1)
