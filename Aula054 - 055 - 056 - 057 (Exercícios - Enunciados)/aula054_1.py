"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
run = True

while run:

    digitado = input('Digite um número inteiro: ')

    try:

        resto = int(digitado) % 2

        if resto == 0:
            print('O número digitado é par.')
        else:
            print('O número digitado é impar.')

    except:

        print('Você não digitou um número inteiro, tente novamente.')

    pergunta = True

    while pergunta:

        prosseguir = input('Deseja fazer outro teste? [S/N]').upper()
        
        if prosseguir == 'N':
            run = False
            break
        elif prosseguir == 'S':
            break