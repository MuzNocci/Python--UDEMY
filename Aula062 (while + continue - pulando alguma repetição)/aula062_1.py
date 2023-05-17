contador = 1

while contador <= 100:

    contador += 1

    if contador >= 10 and contador <= 27:
        print(f'Não vou mostrar o {contador}.')
        continue #passa para o próximo loop do while.

    if contador == 36:
        print('Não vou mostrar o 36.')
        continue #passa para o próximo loop do while.

    print(contador)

    if contador == 40:
        break #finaliza o while.
        
    

print('Acabou!')