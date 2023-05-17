# lista = []

# for numero in range(10):
#     lista.append(numero)

# print(lista)

lista = [
    numero * 2
    for numero in range(10)
    if numero % 2 == 0
]

print(lista)

# É o mesmo que:

lista2 = [numero * 2 for numero in range(10) if numero % 2 == 0]

print(lista2)