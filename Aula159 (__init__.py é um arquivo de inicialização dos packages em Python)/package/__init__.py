print(f'Você importou o package "{__name__}".')

from package.modulo_verificacao import verificacao
from package.modulo_operacoes import *

def dobra(x):
    if verificacao(x):
        return x * 2
    
def triplica(x):
    if verificacao(x):
        return x * 3