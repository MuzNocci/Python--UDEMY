from aula99_package.modulo_verificacao import verificacao

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