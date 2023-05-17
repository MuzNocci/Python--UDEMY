produtos = [
    {'nome':'p1', 'preco':20},
    {'nome':'p2', 'preco':10},
    {'nome':'p3', 'preco':30},
]

novos_produtos = [
    # {'nome': produto['nome'], 'preco': produto['preco']}
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else
    {**produto}
    for produto in produtos
]

print(*novos_produtos, sep='\n')