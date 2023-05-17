def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


# print(
#     executa(
#         lambda x, y: x + y, 2, 3
#     ),

#     executa(soma, 2, 3),

#     soma(2, 3)
# )

    
# print(executa(lambda x, y: x + y, 2, 3))

# print(executa(soma, 2, 3))

# print(soma(2, 3))

# duplica = executa(
#     lambda m: lambda n: n * m, 2
# )

# print(duplica(2))


variables = [1,2,3,4,5,6,7]

print(
    executa(
        lambda *args: sum(args),
        *variables
    )
)