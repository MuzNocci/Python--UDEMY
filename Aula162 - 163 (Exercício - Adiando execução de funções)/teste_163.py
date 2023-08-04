def nome_completo(x, y):
    return x +' '+ y

def cria_funcao(funcao, x):
    def espera(y):
        return funcao(x, y)
    return espera

nome = cria_funcao(nome_completo, 'Müller')

print(nome('Nocciolli'))