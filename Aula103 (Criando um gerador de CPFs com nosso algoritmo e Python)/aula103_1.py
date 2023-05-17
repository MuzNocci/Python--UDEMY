#Gerador de CPF

import random

number_random = ''

for i in range(9):
    number_random += str(random.randint(0,9))

CPF_sum = 0
counter = 10
for number in number_random:
    CPF_sum += int(number) * counter
    counter -= 1
CPF_first_digit = (CPF_sum * 10) % 11
CPF_first_digit = CPF_first_digit if CPF_first_digit < 10 else 0
number_random += str(CPF_first_digit)

CPF_sum = 0
counter = 11
for number in number_random:
    CPF_sum += int(number) * counter
    counter -= 1
CPF_second_digit = (CPF_sum * 10) % 11
CPF_second_digit = CPF_second_digit if CPF_second_digit < 10 else 0
number_random += str(CPF_second_digit)

print(number_random)