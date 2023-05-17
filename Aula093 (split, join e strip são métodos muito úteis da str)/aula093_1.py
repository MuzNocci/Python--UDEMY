'''
split()  = divide uma string
strip()  = retira espaços no final e início da frase ou palavra
lstrip() = retira espaços na esquerda da frase ou palavra
rstrip() = retira espaços na direita da frase ou palavra
join()   = une uma string 
'''

frase = 'Olha só que, coisa interessante'

lista_frase_crua = frase.split(', ')

lista_frase = []

for i, frase in enumerate(lista_frase_crua):
    lista_frase.append(lista_frase_crua[i].strip())

frases_unidas = ', '.join(lista_frase)

print(frases_unidas)