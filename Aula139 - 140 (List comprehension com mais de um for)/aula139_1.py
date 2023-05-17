lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y))

# É o mesmo que:

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

# É o mesmo que:

lista = [(x, y) for x in range(3) for y in range(5)]


print(lista)