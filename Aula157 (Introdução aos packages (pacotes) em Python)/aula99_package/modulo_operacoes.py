from modulo_verificacao import verificacao

def soma(x, y):
    if verificacao(x, y):
        return x + y
    raise('A variável precisa ser número inteiro ou fração.')

def subtracao(x, y):
    if verificacao(x, y):
        return x - y
    raise('A variável precisa ser número inteiro ou fração.')