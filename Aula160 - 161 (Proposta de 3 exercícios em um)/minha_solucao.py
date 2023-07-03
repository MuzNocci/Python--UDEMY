# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

from dados import produtos
import copy

novos_produtos = copy.deepcopy(produtos)
for i in range(len(novos_produtos)):
    novos_produtos[i].update(preco = round(produtos[i]['preco']+(produtos[i]['preco']*10/100),2))
print(*novos_produtos,sep='\n')
print()

produtos_ordenados_por_nome = copy.deepcopy(sorted(produtos, key=lambda dicionario: dicionario['nome'], reverse=True))
print(*produtos_ordenados_por_nome, sep='\n')
print()

produtos_ordenados_por_preco = copy.deepcopy(sorted(produtos, key=lambda dicionario: dicionario['preco']))
print(*produtos_ordenados_por_preco,sep='\n')