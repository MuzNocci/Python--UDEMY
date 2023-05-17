"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome: ').strip(' ')

try:

    if nome.isalpha() and not nome == '':

        if len(nome) <= 4:
            print(f'{nome}, seu nome é curto.')
        elif len(nome) >= 5 and len(nome) <= 6:
            print(f'{nome}, seu nome tem tamanho normal.')
        elif len(nome) > 6:
            print(f'{nome}, seu nome é muito grande.')

    else:

        print('O nome digitado não é um nome válido.')

except:

    print('O nome digitado não é um nome válido.')