'''
Validar CPF
824.176.070-18
'''
print('824', '176', '070', sep='.', end='-')
print('18')

#minha tentativa
CPF = ['824','176','070','18']

for i in range(len(CPF)):
    if i == 2:
        print(CPF[i], end='-')
    elif i >= 3:
        print(CPF[i])
    else:
        print(CPF[i], end='.')
