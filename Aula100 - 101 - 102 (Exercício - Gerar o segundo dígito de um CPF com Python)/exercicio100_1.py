CPF = '746.824.890-70'

CPF_numbers = '%011d' % int(CPF.replace('.','').replace('-',''))
CPF_sum = 0
counter = 10

for number in CPF_numbers:
    if counter >= 1:
        CPF_sum += int(number) * counter
    counter -= 1

CPF_second_digit = (CPF_sum * 10) % 11
CPF_second_digit = CPF_second_digit if CPF_second_digit < 10 else 0
CPF_valid_second_digit = True if CPF_second_digit == int(CPF_numbers[10]) else False

print(CPF_second_digit, CPF_valid_second_digit)