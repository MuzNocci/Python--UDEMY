import sys


iterable = ['Eu', 'Tenho', '__iter__']

iterator = iter(iterable)


lista = [n for n in range(10000)]
#Generatro é uma função que pausa e reinicia
generator = (n for n in range(10000)) #Lista comprehension com Tupla


print(sys.getsizeof(lista))
print(sys.getsizeof(generator))


print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

print(sys.getsizeof(generator))

for num in generator:
    print(num)

