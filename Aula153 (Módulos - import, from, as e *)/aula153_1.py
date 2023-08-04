#import sys
#print(sys.platform)


#from sys import platform
#platform = 'teste' #Sobreescreve a função


from sys import platform as plat, exit as ex

platform = 'teste'

print(platform)
print(plat)


def teste_importacao(name) -> str:
    return f'Olá {name}, você importou o módulo corretamente.'


# Má prática:
#from sys import *
# print(platform) #Importa tudo do módulo