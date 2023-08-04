# *args = recebe argumentos não nomeados

x, y, *resto = 1,2,3,4,5 # o * empacota os dados em uma lista
print(x,y,resto)

def soma(*args): # o *args empacota os dados em uma tupla
    total = 0
    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1,2,3)
print(soma_1_2_3)

soma_4_5_6 = soma(4,5,6)
print(soma_4_5_6)

outra_soma = soma(1,2,3,4,5,6,7,8,9,10)
print(outra_soma)

numeros = 1,2,3,4,5,6,7,8,9,10 # empacota os dados em uma tupla
print(numeros)
print(sum(numeros))

maisumvalor = soma(*numeros) # o * desempacota os dados
print(maisumvalor)