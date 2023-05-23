# Introdução às Generators functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        
        if n >= maximum:
            return #Não retorna nenhum valor, apenas finaliza o loop
    
gen = generator(maximum=5000)

for n in gen:
    print(n)