string = 'muller nocciolli'
metodo = 'upper'

print(dir(string))

if hasattr(string, metodo):
    print(f'Existe {metodo}!')
    print(getattr(string, metodo)())
else:
    print(f'Não existe {metodo}!')



#teste
new_string = string.replace(string[int(string.rfind('u'))], 'ü')
print(new_string.title())


