def gen1():
    yield 1
    yield 2
    yield 3
    
def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6
    
def gen3(gen=None):
    if gen is not None:
        yield from gen()
    yield 7
    yield 8
    yield 9
    
# g = gen1() # Acessa a primeira função
# g = gen2() # Acessa a primeira e a segunda função
# g = gen3() # Acessa a terceira função
# g = gen3(gen1) # Acessa a primeira e a terceira função
# g = gen3(gen2) # Acessa a segunda (que acessa a primeira pelo "yield from gen1()") e a terceira função, executando todas as funções

g = gen3(gen2)

for numero in g:
    print(numero)