'''
while em Python
utilizado para realizar ações enquanto uma condição for verdadeira.

Requesitos: Entender condições e operadores.
'''

#Looping infinito
#while True:
#    pass

x = 0

while x < 5:

    if x == 3:
        x += 1
        continue # vai para o próximo loop

    print(x)
    x += 1