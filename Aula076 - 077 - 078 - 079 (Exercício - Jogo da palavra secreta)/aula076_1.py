import os

os.system('clear') # É que uso Linux, funciona no MAC, no windows é o comando 'cls'

while True:

    secreto = input('Digite a palavra secreta para a FORCA: ')
    
    if secreto.isalpha():

        if len(secreto) > 1:
            secreto = secreto.upper()
            break
        else:
            print('A palavra não pode conter apenas uma letra.')
            continue

    else:

        print('Digite apenas letras.')
        continue

os.system('clear')

base = ''
for i in secreto:
    base += '_'

tentativa = 0

while True:

    while base != secreto:

        resposta = ''
        certo = ''

        letra = input('Digite uma letra: ').upper()
        tentativa += 1

        if letra.isalpha() and len(letra) == 1:

            for c, l in enumerate(secreto):
                if l == letra:
                    resposta += l
                    result = 'e'
                else:
                    if base[c] != '_':
                        resposta += l
                        result = 'j'
                    else:
                        resposta += '_'
                        result = 'n'

            if secreto.find(letra) >= 0 and base.find(letra) < 0:
                print(f'A letra digitada existe na palavra secreta.\nPalavra secreta: {resposta}')
            elif secreto.find(letra) >= 0 and base.find(letra) >= 0:
                print(f'A letra digitada já foi digitada anteriormente.\nPalavra secreta: {resposta}')
            elif secreto.find(letra) < 0:
                print(f'A letra digitada não existe na palavra secreta.\nPalavra secreta: {resposta}')

            base = resposta

        else:

            print('Digite apenas uma letra.')

    else:

        print(f'Você acertou a palavra!\nPrecisou de {tentativa} tentativas para conseguir.')
        break