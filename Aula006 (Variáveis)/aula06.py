'''
Iniciar com letra, pode conter números, separar com _, letras minúsculas
'''
nome = 'Müller'
idade = 36
altura = 1.67
peso = 74
e_maior = idade >= 18
imc = peso / altura**2

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Peso:', peso)
if e_maior:
    maior = 'Sim'
else:
    maior = 'Não'
print('É maior:', maior)
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


print(nome, 'tem' , idade, 'de idade e seu IMC é', imc,'considerado',result_imc+'.')