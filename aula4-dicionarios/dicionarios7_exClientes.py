clientes = {
    'cliente1': {
        'nome': 'Victor',
        'sobrenome': 'Martins'
    },
    'cliente2': {
        'nome': 'Joao',
        'sobrenome': 'Zinho'
    },
    'cliente3': {
        'nome': 'Trynda',
        'sobrenome': 'Mere'
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():  # Lembrando que clientes_v é outro dicioário.
        print(f'\t{dados_k} = {dados_v}')  # \t dá um Tab para ficar mais hierarquizado.
