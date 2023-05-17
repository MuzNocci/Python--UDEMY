'''
Tupla é uma lista imutável.
Sua sintaxe é igual a da lista, porém sem os [] ou com () no lugar dos [].

Tupla é mais rápido do que a lista
'''

nomes = 'Melanie', 'Isabela', 'Muller', 'Lucky', 'Biscoito'

#É possível converter uma lista para tupla e tupla para lista
#Ex:
#nomes = ['Melanie', 'Isabela', 'Muller', 'Lucky', 'Biscoito'] #é uma lista
#nomes = tuple(nomes) #converteu para tupla
#nomes = list(nomes) #converteu para lista


#Ex de erro:
#nomes[2] = 'teste'
#Apresentará erro pois a tupla é imutável

print(nomes[2])
print(nomes[3])
