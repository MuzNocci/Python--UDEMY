# Operadores - IN e NOT IN
# Strings são iteráveis

#  0  1  2  3  4  5
#  M  U  L  L  E  R
# -6 -5 -4 -3 -2 -1

nome = 'Müller'

#print(nome[1]) # retorna 'ü'
#print(nome[-5]) # retorna 'ü'

#print('Mül' in nome) # retorna True
#print('u' in nome) # retorna False 'Diferencia acéntos'

nomeuser = input('Digite seu nome: ')
nomesearch = input('Digite o que deseja encontrar: ')

if nomesearch in nomeuser:
    print(f'{nomeuser}, os caractéres "{nomesearch}", foram encontrados em seu nome.')
else:
    print(f'{nomeuser}, os caractéres "{nomesearch}", não foram encontrados em seu nome.')
