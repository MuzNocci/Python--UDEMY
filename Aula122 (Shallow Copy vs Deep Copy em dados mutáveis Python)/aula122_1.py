import copy

d1 = {
    'c1' : 1,
    'c2' : 2,
    'c3' : [0, 1, 2],
}

d2 = d1 # Não copia, apenas referencia os valores de 'd1'
d3 = d1.copy() # Shallow copy = Não entra em subníveis (Como listas, tuplas, etc... Ex: 'c3')
d4 = copy.deepcopy(d1) # Deep copy = copia em todos os níveis

d2['c1'] = 2 # Altera o valor de 'd1', pois está referenciado e não copiado
d3['c3'][2] = 99
d4['c3'][2] = 2


print(d1)
print(d2)
print(d3)
print(d4)