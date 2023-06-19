# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
import sys
try:
    sys.path.append('/mnt/C09EC9649EC95396/Estudos/Python/Udemy/Aula153 (Módulos - import, from, as e *)')
except ModuleNotFoundError:
    ...

import aula154_2
import aula153_1
import modulos.modulo001
#import modulos.modulo001 as mod001
#from modulos.modulo001 import nameintittle
#from modulos.modulo001 import * #má pratica, pois pode ser sobreposto por alguma variável em seu código que contenha o mesmo nome



print('Módulo: ', __name__)

print(*sys.path, sep='\n')

print(aula153_1.teste_importacao(modulos.modulo001.nameintittle('müller nocciolli')))