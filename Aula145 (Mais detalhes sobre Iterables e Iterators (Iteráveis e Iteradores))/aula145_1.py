iterable = ['Eu', 'Tenho', '__iter__']

iterator = iter(iterable)

for item in range(len(iterable)):
    print(next(iterator))