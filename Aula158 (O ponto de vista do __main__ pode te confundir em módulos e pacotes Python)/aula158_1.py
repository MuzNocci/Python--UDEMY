from aula99_package.modulo_operacoes import soma, subtracao, multiplicacao, divisao


if __name__ == '__main__':

    resultado = divisao(multiplicacao(soma(28, 30), subtracao(50, 11)), 4)

    print(resultado)