'''
Iteravel - str, range, etc
Iterador - quem sabe entregar um valor por vez
next - me entregue o próximo valor
iter - me entregue seu iterador
'''
texto = iter('Muller') # ou .__next__()

print(texto.__next__())
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
