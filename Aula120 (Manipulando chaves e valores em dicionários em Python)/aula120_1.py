people = {}

key = 'Name'
value = 'Melanie'
other_value = 'Müller'

people[key] = value
people['Lastname'] = 'Nocciolli'

print(people[key])

people[key] = other_value


print(people)
print(people[key])

del people[key]
print(people)
print(people.get('Lastname', 'Missing key'))

#people['Name'] = 'Isabela'

if people.get('Name'):
    print(people['Name'])