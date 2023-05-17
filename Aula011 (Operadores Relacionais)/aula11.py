'''
Operadores Relacionais
== #igual
>  #maior 
>= #maiorouigual
<  #menor
<= #menorouigual
!= #diferente
'''
nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

idade_minima = 20
idade_limite = 30

if idade >= idade_minima and idade <= idade_limite:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')