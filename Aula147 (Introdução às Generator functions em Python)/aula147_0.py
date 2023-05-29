def generator(n=0):
    print('Começando...')
    yield 1
    print('Continuando...')
    yield 2
    print('Ainda trabalhando...')
    return "FIM"

#print(next(gen))
#print(next(gen))
    
gen = generator(n=0)

for y in gen:
    print(y)