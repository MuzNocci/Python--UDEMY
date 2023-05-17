# s1 = set()

# s1.add('Muller')
# s1.add(1)

# s1.clear()

# s1.update('Olá mundo')
# s1.update(('Olá mundo',))

# s1.discard('Olá mundo')

#print(s1)


s1 = {1,2,3}
s2 = {2,3,4}

s3 = s1 | s2 # Retorna a união dos sets, sem itens duplicados.
s3 = s1 & s2 # Retorna os items presentse em ambos os sets.
s3 = s1 - s2 # Retorna apenas a diferança apenas do set da esquerda.
s3 = s1 ^ s2 # Retorna a diferença simétrica dos sets.

print(s3)