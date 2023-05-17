'''
Manipulando Strings
- String indices
- Fatiamento de strings
- Funções built-in (len, abs, type, print, etc...)
'''
#indice  [012345678] (positivos)
string = 'Python_s2'
#indice -[987654321] (positivos)

nova_string = string[2:6] # 2 até 5, o último caracter não é lido.
nova_stringi = string[:6] # do início até 5, o último caracter não é lido.
nova_stringf = string[2:] # 2 até o fim, o último caracter não é lido.
nova_stringp = string[0::2] # 0 até o fim e : pulando 2 casas

print(nova_string)
print(nova_stringi)
print(nova_stringf)
print(nova_stringp)
print(f'A string tem {len(string)} caracteres.')