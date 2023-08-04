a, b = 1, 2
a, b = b, a

print(a, b)

pessoa = {
    'nome' : 'Aline',
    'sobrenome' : 'Souza',
}

dados_pessoa = {
    'idade' : 18,
    'altura' : 1.6,
}


pessoa_completa = {**pessoa, **dados_pessoa, 'idade' : 16}
print(pessoa_completa)


# a, b = pessoa.items()
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()

# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)


def argumentos_nomeados(*args, **kwargs):
    print(kwargs)

    for chave, valor in kwargs.items():
        print(chave, valor)


# argumentos_nomeados(nome='Muller', qlq=123, outro='teste')
argumentos_nomeados(**pessoa_completa)