'''
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
'''
texto = 'Python'

#1ª forma
contador = 0
for letra in texto:
    print(contador, letra)
    contador += 1

print('#############################')

#2ª forma
for i , letra in enumerate(texto):
    print(i, letra)