usuario = input('Digite o usuário: ')
senha = input('Digite a senha: ')

user_bd = 'muller'
senha_bd = 'muz'

if (usuario == user_bd or usuario == user_bd.upper()) and senha == senha_bd:
    entrada = 'E'
else:
    entrada = 'S'
    
if entrada == 'E':
    print('Usuário entrou.')
elif entrada == 'S':
    print('Usuário ou senha incorreto.')