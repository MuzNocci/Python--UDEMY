"""
Calculo do primeiro dígito do CPF

CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
CPF = '746.824.890-70'

CPF_numbers = '%011d' % int(CPF.replace('.','').replace('-',''))
CPF_sum = 0
counter = 10

for number in CPF_numbers:
    if counter >= 2:
        CPF_sum += int(number) * counter
    counter -= 1

CPF_first_digit = (CPF_sum * 10) % 11
CPF_first_digit = CPF_first_digit if CPF_first_digit < 10 else 0

print(CPF_first_digit)

CPF_valid_first_digit = True if CPF_first_digit == int(CPF_numbers[9]) else False


