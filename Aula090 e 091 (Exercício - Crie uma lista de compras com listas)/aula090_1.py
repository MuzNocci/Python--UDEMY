import os
os.system('clear')
lista = []

while True:

    print('O que deseja fazer?')
    print('[i]nserir | [a]pagar | [l]istar')
    escolha = input('Escolha uma opção: ').lower()

    if escolha == 'i' or escolha == 'a' or escolha == 'l':

        os.system('clear')

        if escolha == 'i':

            while True:

                item = input('Digite o item que deseja inserir: ')
                
                if item == '':

                    os.system('clear')
                    print('Digite um item para sua lista!')
                    continue

                else:

                    os.system('clear')
                    lista.append(item)
                    break

        elif escolha == 'a':

            while True:

                if len(lista) > 0:

                    print('Confira sua lista:')
                    for indice, item in enumerate(lista):
                        print(f'{indice} - {item}')

                    print('')

                    try:

                        item = int(input('Digite o número item que deseja apagar: '))
                    
                    except:

                        os.system('clear')
                        print('Digite um item existente na lista, para que possa apagar!\n')
                        break
                        
                
                    if item == '' or item > len(lista):

                        os.system('clear')
                        print('Digite um item existente na lista, para que possa apagar!\n')
                        continue

                    else:

                        os.system('clear')
                        lista.pop(item)
                        break

                else:

                    os.system('clear')
                    print('A lista está vazia!\n')
                    break

        elif escolha == 'l':

            if len(lista) > 0:
                print('Confira sua lista:')
                for indice, item in enumerate(lista):
                    print(f'{indice} - {item}')

                print('')

            else:

                os.system('clear')
                print('A lista está vazia!\n')
                continue

    else:

        os.system('clear')
        print('A opção digitada não é válida!!!\n')
        continue