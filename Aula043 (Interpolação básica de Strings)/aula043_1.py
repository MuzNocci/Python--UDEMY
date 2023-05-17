def cammel(name):
    pronto = ''
    c = 0
    for i in name:
        if c == 0:
            pronto += i.upper()
        else:
            pronto += i.lower()    
        c += 1
    return pronto

nome = input('Digite seu primeiro nome: ')
preco = 1000.9515
variavel = f'{cammel(nome)}, o preço é R$ {preco:,.2f}.'

print(variavel)