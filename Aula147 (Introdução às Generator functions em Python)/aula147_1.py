# Introdução às Generators functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        
        if n >= maximum:
            return #Não retorna nenhum valor, apenas finaliza o loop
    
def generator2(n=0, maximum=10):
    while True:
        print(n)
        n += 1
        
        if n >= maximum:
            return #Não retorna nenhum valor, apenas finaliza o loop
        
        
gen = generator(maximum=10) # Devolve um iteravel

for n in gen:
    print(n)


gen2 = generator2(maximum=10) # Apenas imprime os valores na tela