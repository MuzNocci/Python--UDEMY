# Fatiamento de Strings e Função LEN

variavel = 'Olá mundo'

#variavel[inicio : fim : passo]
print(variavel[2:7:2]) #resultado 'ámn'

#len conta a quantidade de caracteres da variável.
print(len(variavel)) # 9 Caracteres

print(variavel[0:len(variavel):2]) # é igual a [0::2]

print(variavel[::-1]) #inverte a variável
