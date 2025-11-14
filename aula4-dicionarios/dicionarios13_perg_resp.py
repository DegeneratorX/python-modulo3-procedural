perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'resposta': {'a': '1', 'b': '4', 'c': '5'},
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'resposta': {'a': '4', '10': '4', 'c': '6'},
        'resposta_certa': 'c'
    },
}

respostas_certas = 0

for pk, pv in perguntas.items():  # pk = pergunta (key) / pv = pergunta (valor)
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['resposta'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input("Sua resposta: ")

    if resposta_usuario == pv['resposta_certa']:
        print("Parabéns, você acertou")
        respostas_certas += 1
    else:
        print("Você errou!")
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Porcentagem de acerto: {porcentagem_acerto}%')
