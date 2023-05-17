'''
Formatando valores com modificadores
 
:s - Texto (string)
:d - Inteiro (int)
:f - Número de ponto flutuante (float)
:.(número)f - Quantidade de casas decimais (float)
:(caracter)(> ou < ou ^)(quantidade)(tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro

'''
num = input('Digite um número inteiro: ')

#As duas linhas abaixo exibem a mesma coisa:
print(f'{num:0>5}')
print(f'{num.rjust(5,"0")}')

print(f'{num.ljust(5,"0")}')