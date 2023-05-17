letras = set()

while True:

    letra = input('Digite a letra: ').lower()
    if letra in letras:
        print('Você á digitou essa letra!')
    
    letras.add(letra)

    if 'l' in letras:
        print('Parabéns!')
        break

    print(letras)

