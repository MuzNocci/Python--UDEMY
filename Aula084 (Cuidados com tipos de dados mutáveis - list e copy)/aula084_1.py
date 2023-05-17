nome = 'Muller'
# nome[1] = 'ü' # vai dar erro

outro_nome = nome

nome = 'Melanie'

print(nome)
print(outro_nome)


lista_a = ['Muller', 'Isabela', 'Melanie']
lista_b = ['Lucky', 'Biscoito']

lista_c = lista_b #aponta para o mesmo endereço na memória

lista_d = lista_b.copy() #cria novo endereço na memória com cópia da lista

familia = lista_a + lista_b #cria novo endereço na memória

lista_b[1] = 'Dori'

print(id(familia))
print(id(lista_b))
print(id(lista_c))
print(id(lista_d))