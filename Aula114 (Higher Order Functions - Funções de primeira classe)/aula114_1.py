'''
Higher Order Functions
Fuções de primeira classse
'''
def salutation(hour, name):
    salutation = ''
    if hour < 12:
        salutation = 'bom dia'
    elif hour > 11 and hour < 18:
        salutation = 'boa tarde'
    elif hour > 17 and hour < 24:
        salutation = 'boa noite'
    return f'{name}, {salutation}!' if salutation else f'{name}, bom dia, boa tarde, boa noite! Nem sei que horas são...'

# def executa(funcao, hour, name):
#     return funcao(hour, name)
# ou
def executa(funcao, *args):
    return funcao(*args)


print(executa(salutation, 10, 'Müller'))
