usuario = input('Digite seu usuário: ').strip()

qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Número inválido de caracteres.')
else:
    print(f'{usuario} foi cadastrado no sistema.')
