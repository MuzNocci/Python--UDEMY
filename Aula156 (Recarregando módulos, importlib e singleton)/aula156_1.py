import importlib

import aula156_2

print(aula156_2.variavel)


for i in range(10):
    #import aula156_2 # Não importa novamente, pois os imports são singletons e não são executados duas vezes
    importlib.reload(aula156_2)
    print(i)