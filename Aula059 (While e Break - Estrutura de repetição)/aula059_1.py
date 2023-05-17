"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira.
Loop infinito -> Quando um código não tem fim.
"""
condicao = True

while condicao:
    nome = input('Digite seu nome: ')
    

    if nome == 'sair':
        print('Tchau!!!')
        break
    else:
        print(f'Seu nome é {nome}.')