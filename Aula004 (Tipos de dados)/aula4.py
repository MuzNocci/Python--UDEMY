'''
Tipos de dados:
str - string = Textos 'Assim' "Assim"
int - inteiro = número interio "0 -10 20 -40"
float - real/ponto flutuante = número fracionado "0.5 15.9 -20.6"
bool - booleano/lógico = Verdeiro ou Falso "True or False"
'''
print('Luiz:', type('Luiz'))
print('10:', type(10))
print('20.6:', type(20.6))
print('True:', type(True))
print('ou 10 == 10:', type(10 == 10))
print('ou \'L\' == \'t\':', type('L' == 't'))
print('Luiz', type('Luiz'), bool('Luiz'))
#type casting (Alteração de tipo de dados)
print('10', type('10'), type(int('10')))
print('10' , type('10'), type(float('10')), float('10'))