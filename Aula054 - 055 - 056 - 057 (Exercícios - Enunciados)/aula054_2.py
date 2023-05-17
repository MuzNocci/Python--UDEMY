"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

nome = input('Digite seu nome: ')
horario = input('Digite a hora (HH:MM): ')

try:

    horario = horario.split(':')
    hora = int(horario[0])
    minuto = int(horario[1])

    if hora >= 0 and hora <= 11:
        print(f'Bom dia {nome}!')
    elif hora >=12 and hora <= 17:
        print(f'Boa tarde {nome}!')
    elif hora >= 18 and hora <= 23:
        print(f'Boa noite {nome}!')

except:

    print(f'{nome}, o valor digitado não é uma hora válida.')