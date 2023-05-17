def valid_cpf(CPF):

    try:

        CPF = CPF.replace('.','').replace('-','')

        def first_digit(CPF):

            CPF_sum = 0
            counter = 10

            for number in CPF[:9]:
                CPF_sum += int(number) * counter
                counter -= 1

            CPF_first_digit = (CPF_sum * 10) % 11
            CPF_first_digit = CPF_first_digit if CPF_first_digit < 10 else 0
            
            return True if CPF_first_digit == int(CPF[9]) else False


        def second_digit(CPF):

            CPF_sum = 0
            counter = 11

            for number in CPF[:10]:
                CPF_sum += int(number) * counter
                counter -= 1

            CPF_second_digit = (CPF_sum * 10) % 11
            CPF_second_digit = CPF_second_digit if CPF_second_digit < 10 else 0
            
            return True if CPF_second_digit == int(CPF[10]) else False


        print('O CPF é válido!' if first_digit(CPF) and second_digit(CPF) and CPF != (CPF[0] * len(CPF)) else 'O CPF não é válido!')


    except:

        print('O CPF não é válido!')


while True:

    valid_cpf(input('Digite o CPF para validação: '))