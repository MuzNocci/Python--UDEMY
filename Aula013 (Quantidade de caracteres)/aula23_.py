'''
Função len()

OBS: Só funciona com strings
'''
usuario = input('Digite seu usuario: ').strip()
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres.')
else:
    print('Você foi cadastrado no sistema.')