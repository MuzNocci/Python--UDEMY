# Descompactamento em chamadas
# de metodos e funções

string = 'ABCD'
lista = ['Maria','Helena',1,2,3,'Eduarda']
tupla = 'Python','é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0       1       2          3
    ['Luiz', 'João', 'Eduarda', (0,10,20,30,40)], # 2
]

for nome in lista:
    print(nome, end=' ')

print(*lista)

print(*string)

print(*tupla)

print(*salas)