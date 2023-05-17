'''
+  = adição
-  = subtração
*  = multiplicação
/  = divisão
// = divisão (inteiro)
** = potenciação
%  = resto da divisão
() = altera precedência

Precedência de operadores:
1. ( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro
2. ** - Depois vem a exponenciação
3. * / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo
4. +  - - Por fim, soma e subtração
'''

print('Adição +', 10 + 10)
print('Subtração -', 10 - 5)
print('Multiplicação *', 10 * 10)
print('Multiplicação de string', 3 * 'Müller')
print('Divisão /', 10 / 2)
print('Divisão //', 10 // 3)
print('Potenciação **', 4 ** 2)
print('Resto da divisão %', 10 % 3)
print('Precedência', 10 + 15 * 3)
print('Alteração de precedência ()', 10 * (15 + 3))