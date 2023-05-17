''' 
Faça um programa que peça ao usuário para digitar um número interio:
informe se este número é par ou impar.
Caso o usuário não digite um núemro inteiro, informe que não é um número inteiro.
'''
num = input('Digite um número inteiro: ')

if num.isnumeric():
    resto = int(num) % 2
    if resto != 0:
        print(f'O número {num} é impar.')
    else:
        print(f'O número {num} é par.')
else:
    print('O caracter digitado não é um número inteiro.')