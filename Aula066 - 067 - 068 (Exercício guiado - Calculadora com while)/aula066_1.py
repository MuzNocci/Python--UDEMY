"""
Calculadora com while
"""

####### Funções ########
def verify_type(var):

    result = None

    try:

        n = 0
        p = 0
        o = 0

        for char in var:
            if char.isnumeric():
                n += 1
            elif char == '.' or char == ',':
                p += 1
            else:
                o += 1


        if n > 0 and p == 0 and o == 0:
            result = 'int'
        elif n > 0 and p > 0 and o == 0:
            result = 'float'
        else:
            result = 'str'

    except:

        result = None

    return result

########## Início da Aplicação ##########
calculadora = True

while calculadora:


    print('##### Bem vindo a sua calculadora! #####')


    n1 = input('Digite um número inteiro: ')
    while verify_type(n1) != 'int' and verify_type(n1) != 'float':
        print('O número digitado é inválido!')
        n1 = input('Digite um número inteiro: ')

    print('Utilize um dos operadores:')
    print('"+" Adição | "-" Subtração | "*" Multiplicação | "/" Divisão')
    op = input('Digite o operador: ')
    while not op == '+' and not op == '-' and not op == '*' and not op == '/':
        print('O operador digitado é inválido!')
        print('Utilize um dos operadores:')
        print('"+" Adição | "-" Subtração | "*" Multiplicação | "/" Divisão')
        op = input('Digite o operador: ')

    n2 = input('Digite outro número inteiro: ')
    while verify_type(n2) != 'int' and verify_type(n2) != 'float':
        print('O número digitado é inválido!')
        n2 = input('Digite outro número inteiro: ')


    try:

        if verify_type(n1) == 'int':
            n1 = int(n1)
        elif verify_type(n1) == 'float':
            n1 = float(n1)
        
        if verify_type(n2) == 'int':
            n2 = int(n2)
        elif verify_type(n2) == 'float':
            n2 = float(n2)

        if op == '+':
            resultado = n1 + n2
        elif op == '-':
            resultado = n1 - n2
        elif op == '*':
            resultado = n1 * n2
        elif op == '/':
            resultado = n1 / n2
        else:
            print('Ocorreu um problema com os valores digitados.')
            continue

    except:

        print('Ocorreu um problema com os valores digitados.')
        continue


    print(f'O resultado é: {resultado}')

    sair = input('Deseja sair da calculadora? [s]im: ').lower()

    if sair == 's' or sair == 'sim':
        break