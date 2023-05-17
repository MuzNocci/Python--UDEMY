#É a forma mais precisa para trabalhar com números decimais.

import decimal

numero_1 = decimal.Decimal('0.1') #Converte string para decimal
numero_2 = decimal.Decimal('0.7') #Funciona apenas para string, não para números.
numero_3 = numero_1 + numero_2

print(numero_3)