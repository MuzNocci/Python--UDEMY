"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +

Create,   Read,   Update,   Delete    =    CRUD
Criar,    Ler,    Alterar,  Apagar
"""

#indices   0    1     2                   3    4
#         -5   -4    -3                  -2   -1
lista =   [123, True, 'Müller Nocciolli', 1.2, [5, 6, False]]
outralista = [False, 'São Paulo', 1985, 'Ribeirão Preto', 2009,'Campos dos Goytacazes']
novalista = [15, 30, 99, 'Teste de Lista']


#Exemplos:

lista[2] = 'Müller Ribeiro' #Atualiza o item da lista

del lista[3] #Deleta o item da lista

lista.append(50) #Adiciona o item ao final da lista

lista.append(60)

lista.insert(0,'Testando') #Adiciona o item ao índice indicado

#lista.pop() - remove o último item da lista
removido_lista = lista.pop(1) #Remove o item indicado da lista


#Exibe a lista:

for item in lista:
    print(item, type(item))

print(f'O item "{removido_lista}" foi removido.')

