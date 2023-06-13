# Exemplo
try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as error:
    print(error.__class__.__name__.upper())
    print(str(error).upper())
else:
    print('NÃO DEU ERRO')
finally:
    print('FECHAR ARQUIVO')