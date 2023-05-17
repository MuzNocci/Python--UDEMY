'''
Listas em Python
fatiamento

append #insere valor no final da lista
insert #insere valor no começo da lista
pop    #remove valor do indice indicado
del    #deleta elemento da lista


, clear, extend, +
min , max
range
'''
l1 = ['A','B','C', 0, 6, 10]
l2 = ['D','E', 10.5, 8]

print('Lista 1:', l1)
print('Lista 2:', l2)

del(l1[3:6])
l2.pop()
l2.insert(2,'F')
l2.pop(3)
l2.append('G')

print('############')

print('Lista 1 tratada:', l1)
print('Lista 2 tratada', l2)

print('############')
l3 = l1 + l2
print('Lista consolidada com +:', l3)

l1.extend(l2)
print('Lista consolidada com extend:', l1)

print('############')

print('Quantidade de itens na lista:',len(l3))
#max e min, funcionam para números e letras.
print('Maior item na lista:',max(l3))
print('Menor item na lista:',min(l3))
