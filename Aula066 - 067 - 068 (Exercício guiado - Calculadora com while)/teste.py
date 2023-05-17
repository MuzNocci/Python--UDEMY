#funções
def verify_type(var):

    try:

        n = 0
        p = 0
        o = 0

        for char in var:
            if char.isnumeric():
                n += 1
            elif char == '.' or char == ',':
                p += 1
            else:
                o += 1


        if n > 0 and p == 0 and o == 0:
            result = 'int'
        elif n > 0 and p > 0 and o == 0:
            result = 'float'
        else:
            result = 'str'

    except:

        result = None

    return result


text = input('Digite text: ')

print(type(text))

print(verify_type(text))