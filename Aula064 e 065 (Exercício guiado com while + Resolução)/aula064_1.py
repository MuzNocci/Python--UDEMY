"""
Iterando strings com while
"""

nome = 'Müller Nocciolli' # Strings são iteraveis
tamanho_nome = len(nome)
letras = len(nome.replace(' ', ''))
nome_completo = f'{nome} Ribeiro'

print(nome)
print(letras)
print(tamanho_nome)
print(nome[4])
print(nome_completo)


novo_nome = '*'

for char in nome:
    novo_nome += f'{char}*'

print(novo_nome)


wnovo_nome = '*'
contador = 0

while contador < tamanho_nome:

    wnovo_nome += f'{nome[contador]}*'
    contador += 1

print(wnovo_nome)

