'''
Faça uma calculadora de idade e de IMC.
'''
from datetime import date

data = str(date.today())
hoje = data.split('-')
ano = int(hoje[0])
mes = int(hoje[1])
dia = int(hoje[2])

nome = 'Lucky'
altura = 1.67
peso = 72
data_nascimento = '22/05/1985'

nasci = data_nascimento.split('/')
nasci_dia = int(nasci[0])
nasci_mes = int(nasci[1])
nasci_ano = int(nasci[2])

idade = ano - nasci_ano
if mes < nasci_mes:
    idade = idade-1
else:
    if mes == nasci_mes:
        if dia < nasci_dia:
            idade = idade-1

imc = peso / altura**2
if imc >= 18.5 and imc <= 24.9:
    result_imc = 'normal'
elif imc >= 25.0 and imc <= 29.9:
    result_imc = 'sobrepeso'
elif imc >= 30.0 and imc <= 39.9:
    result_imc = 'obesidade'
elif imc >= 40.0:
    result_imc = 'obesidade grave'
else:
    result_imc = 'fora dos padrões conhecidos'

print(f'{nome} tem {idade} anos de idade, tem {altura:.2f}m altura e pesa {peso:.1f}kg.\nO IMC de {nome} é {imc:.2f}, considerado {result_imc}.')