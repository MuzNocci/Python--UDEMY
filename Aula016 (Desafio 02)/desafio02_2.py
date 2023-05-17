''' 
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada.Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
'''
horario = input('Digite a hora (HH:MM): ').strip().split(':')

try:

    hora =  int(horario[0])
    minuto = int(horario[1])

    if hora >= 0 and hora <=23 and minuto >= 0 and minuto <= 59:
        if hora >= 0 and hora <= 11:
            print(f'Bom dia! Agora são {hora:0>2}:{minuto:0>2}h.')
        elif hora >=12 and hora <=17:
            print(f'Boa tarde! Agora são {hora}:{minuto:0>2}h.')
        elif hora >=18 and hora <=23:
            print(f'Boa noite! Agora são {hora}:{minuto:0>2}h.')
    else:
        print('O horário digitado é inválido.')

except:

    print('O horário digitado é inválido.')