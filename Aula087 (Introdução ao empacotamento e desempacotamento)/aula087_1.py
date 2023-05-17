nomes = ['Melanie', 'Isabela', 'Muller', 'Lucky', 'Biscoito']
nome1, nome2, nome3, nome4, nome5 = nomes

#Outra forma de definir
#nome1, nome2, nome3 = ['Melanie', 'Isabela', 'Muller']

#Outra forma é: A primeira variável pela o primeiro valor, a segunda pega o segundo e o resto "*_" pega os demais.
_, nome2, *_ = nomes

print(nome2)