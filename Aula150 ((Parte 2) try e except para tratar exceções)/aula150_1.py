try:
    a = 18
    b = int(input('Digite um número:'))
    
    c = a / b
    
    print(f'A divisão de 18 por {b} é {c}.')

except ZeroDivisionError:
    print('Dividiu por zero.')
    
except ValueError:
    print('Dividiu por um caracter não "Inteiro".')
    
except (TypeError, IndexError):
    print('Dividiu por um caracter não "Inteiro".')
    
except NameError:
    print('O valor não foi definido.')
    
except:
    print('Erro desconhecido.')
    
finally:
    ...
    
print('Fim do código.')