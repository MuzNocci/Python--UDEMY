frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido Van Rossum.'

i = 0
qtd_mais_vezes = 0
letra_mais_vezes = 0

while i < len(frase):
    
    letra_atual = frase[i]
    quantidade_letra_apareceu = frase.count(letra_atual)

    if qtd_mais_vezes < quantidade_letra_apareceu and not letra_atual == ' ':
        qtd_mais_vezes = quantidade_letra_apareceu
        letra_mais_vezes = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_mais_vezes}", que apareceu {qtd_mais_vezes} vezes.')