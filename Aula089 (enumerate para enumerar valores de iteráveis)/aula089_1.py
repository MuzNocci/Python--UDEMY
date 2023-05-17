nomes = ['Melanie', 'Isabela', 'Muller', 'Lucky', 'Biscoito']

for item in enumerate(nomes):
    indice, nome = item
    print(indice, nome)

#ou

for indice, nome in enumerate(nomes):
    print(indice, nome)

#ou

for item in enumerate(nomes):
    for valor in item:
        print(valor)