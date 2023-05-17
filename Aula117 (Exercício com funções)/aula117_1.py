def double(number) -> int:
    return int(number) * 2

def triple(number) -> int:
    return int(number) * 3

def quadruple(number) -> int:
    return int(number) * 4

x = 5
print(f'Você informou o valor {x}.')
print(f'O drobro de {x}, é {double(x)}.')
print(f'O triplo de {x}, é {triple(x)}.')
print(f'O quadruplo de {x}, é {quadruple(x)}.')