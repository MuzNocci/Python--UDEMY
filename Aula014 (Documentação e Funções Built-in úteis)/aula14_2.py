num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

try:
    num1 = int(num1)
    num2 = int(num2)
    print(num1+num2)
except:
    print('Não pude converter os números para realizar contas')