"""
Closures - Fechamentos

Closures são funções internas que capturam e "lembram" do estado das variáveis 
do escopo externo, mesmo após esse escopo ter sido finalizado.
"""

# Exemplo de closure simples
def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!' # A função interna acessa as variáveis do escopo externo.
    return saudar

# Criando closures. Perceba que cada chamada cria uma nova função com seu próprio estado.
saud_1 = criar_saudacao('Bom dia', 'Ana')
saud_2 = criar_saudacao('Boa noite', 'Ana')

# Nesse ponto do código, as funções internas 'saudar' ainda têm acesso às variáveis 'saudacao' e 'nome' (sim, elas não foram perdidas),
# mesmo que a função externa 'criar_saudacao' já tenha terminado sua execução. É loucura, mas
# é assim que closures funcionam em Python. Para provar isso, veja o endereço de memória delas:
print(f"Endereço de memória da função saud_1: {id(saud_1)}") # Esse endereço será diferente do saud_2. Ele guarda o estado da closure.
print(f"Endereço de memória da função saud_2: {id(saud_2)}")

# Testando as closures
print(saud_1())
print(saud_2())

print("\n################################################\n")



"""
Criador de funções com closures

Um uso avançado de closures é criar funções personalizadas com base em parâmetros fornecidos
à função externa. Isso permite a criação de funções especializadas de forma dinâmica.

Essa técnica é útil para criar fábricas de funções, onde a função externa configura o comportamento
da função interna com base nos argumentos fornecidos. Muito utilizada em programação funcional.
"""

def criar_saudacao_personalizada(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'  # A função interna usa o parâmetro da função externa.
    return saudar

falar_bom_dia = criar_saudacao_personalizada('Bom dia')
falar_boa_noite = criar_saudacao_personalizada('Boa noite')

print(falar_bom_dia('Ana'))
print(falar_boa_noite('Ana'))

for nome in ['Maria', 'João', 'Pedro']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))