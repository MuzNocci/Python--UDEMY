import os

os.system('clear')

secreto = input('Digite a palavra secreta para a FORCA: ')
    
os.system('clear')

base = ''
for i in secreto:
    base += '_'

while True:

    while base != secreto:

        resposta = ''
        certo = ''

        letra = input('Digite uma letra: ')

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
        print(f'Você acertou a palavra!')
        break