def fatorial(n):
    """Calcula o fatorial de um número n."""
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

def fibonacci(n):
    """Retorna o n-ésimo número da sequência de Fibonacci."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

variavel_de_modulo = "Variável do módulo 3"