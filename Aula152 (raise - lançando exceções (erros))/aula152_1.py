def divide_por_zero(d):

    if d == 0:
        raise ZeroDivisionError('Não é possível dividir por zero.')
    
    return True

def check_value(d):

    if not isinstance(d, (float, int)):
        raise TypeError(
            f'"{d}" deve ser int ou float.'
        )

def divide(n, d):

    check_value(d)
    check_value(n)
    divide_por_zero(d)

    return n / d


print(divide(8, 'e'))