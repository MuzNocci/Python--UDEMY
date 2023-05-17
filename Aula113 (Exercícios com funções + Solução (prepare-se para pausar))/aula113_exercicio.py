# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

#Crie uma função que fala se um número é par ou ímpar.
#Retorne se o número é par ou ímpar.

def multiply(*args) -> int:
    result = 1
    for number in args:
        result *= number
    return result

def even_or_odd(number) -> str:
        return 'par' if (number % 2) == 0 else 'ímpar' # operação ternária


print(f'O resultado da multiplicação dos múmeros é {multiply(1,2,3,4,5,6,7)}, e esse número é {even_or_odd(multiply(1,2,3,4,5,6,7))}.')