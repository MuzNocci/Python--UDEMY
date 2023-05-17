'''
While / Else
contadores
acumuladores
'''

contador = 1

acumulador = 1


while contador <= 10: #inicia o laço

    print(contador, acumulador)

    if contador > 5:
        break #sai do laço

    acumulador = acumulador + contador
    contador += 1

else:
    print('Cheguei no else')