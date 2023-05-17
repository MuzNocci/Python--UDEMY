# O 'not' inverte a expressão (True => False e False => True).

senha = input('Senha: ')

if senha == '123':
    print('entrou')
else:
    if not senha:
        print('Digite a senha')
    else:
        print('Senha incorreta')