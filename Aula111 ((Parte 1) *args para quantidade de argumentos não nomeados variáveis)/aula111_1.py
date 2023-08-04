def soma2(x, y, *resto):
     print(x, type(x))
     print(y, type(y))
     print(resto, type(resto))
     for item in resto:
          print(item, type(item))

def soma(*args):
    print(args, type(args))
    args = list(args)
    args[1] = 8
    print(args, type(args))
    args = tuple(args)
    print(args, type(args))

    total = 0
    for item in args:
         total += item
    print('Total:',total)

soma(1,2,3,4,5)
soma2(1,2,5,2,2,72,9)