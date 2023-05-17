# Descompactamento em chamadas
# de metodos e funções

string = 'ABCD'
lista = ['Maria','Helena',1,2,3,'Eduarda']
tupla = 'Python','é', 'legal'

a, b, *_, c = lista

d, e, f = tupla

print(a, c, e, f)