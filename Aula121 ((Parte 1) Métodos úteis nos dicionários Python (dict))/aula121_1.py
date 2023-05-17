# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

people = {
    'Name' : 'Müller',
    'Lastname' : 'Nocciolli',
}
people.setdefault('Idade', 0)

print(list(people.keys()))
print(list(people.values()))
print(list(people.items()))
print(len(people))
print(people['Name'])

for key in people:
    print(key, people[key])

for key, value in people.items():
    print(f'{key}: {value}')