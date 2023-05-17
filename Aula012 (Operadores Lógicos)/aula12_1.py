usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'muz'
senha_bd   = '123'

if usuario == usuario_bd and senha == senha_bd:
    print('Usuário logado.')
else:
    print('Usuário ou senha inválido')