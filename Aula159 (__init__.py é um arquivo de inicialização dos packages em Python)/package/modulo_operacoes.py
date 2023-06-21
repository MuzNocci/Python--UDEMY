from package.modulo_verificacao import verificacao

__all__ = [
    'soma',
    'subtracao',
    'multiplicacao',
    'divisao',
]

def soma(x, y):
    if verificacao(x, y):
        return x + y
    raise('As variáveis precisam ser número inteiro ou fração.')

def subtracao(x, y):
    if verificacao(x, y):
        return x - y
    raise('As variáveis precisam ser número inteiro ou fração.')

def multiplicacao(x, y):
    if verificacao(x, y):
        return x * y
    raise('As variáveis precisam ser número inteiro ou fração.')

def divisao(x, y):
    if verificacao(x, y):
        return x / y
    raise('As variáveis precisam ser número inteiro ou fração.')

def divisaointeira(x, y):
    if verificacao(x, y):
        return x // y
    raise('As variáveis precisam ser número inteiro ou fração.')