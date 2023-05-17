print('Exercício: Teste de conhecimentos.')

nomestatus = False

while nomestatus == False:
    
    nome = input('Digite seu nome: ').strip()
    nomesemescaco = nome.replace(' ','')
    
    if nome == '':
        print('O campo "Nome" é obrigatório!')
    elif not nomesemescaco.isalpha() and not ' ' in nome:
        print('O campo "Nome" deve conter apenas letras e espacos!')
    else:
        nomestatus = True

idadestatus = False

while idadestatus == False:
    
    idade = input('Digite sua idade:')
    
    if idade == '':
        print('O campo "Idade" é obrigatório!')
    elif not idade.isnumeric():
        print('O campo "Idade" deve ser apenas números!')
    else:
        idadestatus = True
        
print(f'Seu nome é {nome}.')
print(f'Seu nome invertido é {nome[::-1]}.')
if ' ' in nome:
    print(f'Seu nome contem espaços.')
else:
    print(f'Seu nome não contem espaços.')
print(f'Seu nome tem {len(nomesemescaco)} letras.')
print(f'A primeira letra do seu nome é "{nome[0]}".')
print(f'A última letra do seu nome é "{nome[-1]}".')
print(f'Você tem {idade} anos de idade.')