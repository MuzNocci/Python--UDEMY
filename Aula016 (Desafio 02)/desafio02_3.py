''' 
Faça um programa que peça o primeiro nome do usuário.
Se o nome tiver 4 letras ou menos escreva 'Seu nome é curto';
se tiver entre 5 e 6 letras, escreva 'Seu nome é normal';
se for maior que 6 escreva 'Seu nome é muito grande'.
'''
nome = input('Digite seu nome: ').strip()

if len(nome) <= 4 and len(nome) > 0:
    print(f'{nome}, seu nome é curto.')
elif len(nome) == 5 or len(nome) == 6:
    print(f'{nome}, seu nome é normal.')
elif len(nome) > 6:
    print(f'{nome}, seu nome é muito grande.')
else:
    print('Digite um nome válido.')