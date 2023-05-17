while True:

    num1 = input('Digite um número: ')
    operador = input('Digite um operador: ')
    num2 = input('Digite outro número: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        result = num1 / num2
    else:
        print('Operador inválido.')
        continue
    
    print(f'O resultado do cálculo é: {result}\n')
    sair = input('Deseja sair? [s]im ou [n]ão: ')
    print('')

    if sair == 's':
        break
