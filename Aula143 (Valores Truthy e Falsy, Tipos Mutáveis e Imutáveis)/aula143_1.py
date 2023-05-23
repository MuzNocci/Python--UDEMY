lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ""
inteiro = 1
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'Lista:{lista}', falsy(lista))
print(f'Dicionário:{dicionario}', falsy(dicionario))
print(f'Conjunto:{conjunto}', falsy(conjunto))
print(f'Tupla:{tupla}', falsy(tupla))
print(f'String:{string}', falsy(string))
print(f'Inteiro:{inteiro}', falsy(inteiro))
print(f'Flutuante:{flutuante}', falsy(flutuante))
print(f'Nada:{nada}', falsy(nada))
print(f'Falso:{falso}', falsy(falso))
print(f'Intervalo:{intervalo}', falsy(intervalo))
