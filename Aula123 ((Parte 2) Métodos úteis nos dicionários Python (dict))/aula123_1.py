people = {
    'Name' : 'Müller',
    'Lastname' : 'Nocciolli',
}

# Atribui o valor para variável e deleta o campo do dicionário.
#name = people.pop('Name')

# Atribui o valor da última chave e deleta ela do dicionário.
#name = people.popitem() 

# Atualiza os valores das chaves e adiciona caso não existam no dicionário.
#people.update({
#    'Name' : 'Melanie',
#    'Age' : 9,
#})

tuple = (('Name', 'Isabela'), ('Age', 30))
lista = [['Name', 'Isabela'], ['Age', 30]]

people.update(tuple)

print(people)