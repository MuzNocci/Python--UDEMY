'''
Closure e funções que retornam outras funções
'''

def create_salutation(salutation):
    def salute(name):
        return f'{salutation}, {name}!'
    return salute


speak_goodmorning = create_salutation('Good morning')
speak_goodnight = create_salutation('Good night')

for nome in ['Müller', 'Melanie', 'Isabela', 'Lucky']:
    print(speak_goodmorning(nome))
    print(speak_goodnight(nome))