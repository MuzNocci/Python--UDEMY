numero = input('Vou dobrar o número que você digitar: ')

try:
    numero_float = float(numero)
    print(f'O dobro de {numero} é {numero_float * 2:.2f}.')
except:
    print('O valor digitado não é um número.')