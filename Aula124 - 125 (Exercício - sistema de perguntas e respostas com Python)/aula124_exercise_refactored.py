import os

letters = [
    {
        '0' : 'A',
        '1' : 'B',
        '2' : 'C',
        '3' : 'D',
     }
]

questions = [
    {
        'Question' : 'How much is 2 + 2?',
        'Options' : ['1','2','3','4'],
        'Answer' : '4',
    },
    {
        'Question' : 'How much is 5 * 5?',
        'Options' : ['25','55','10','51'],
        'Answer' : '25',
    },
    {
        'Question' : 'How much is 10 / 2?',
        'Options' : ['4','5','2','1'],
        'Answer' : '5',
    },
]

os.system('clear')
print('########################################')
print('Welcome to Math Test 2.0')
print('########################################\n')
name = input("What's your name? ")

counter = 0
hit = 0
answers = {}

for quest in questions:

    os.system('clear')
    counter += 1
    answer = ''

    print(f"{name}, {quest['Question'].lower()}\n")

    for i, option in enumerate(quest['Options']):
        for letter in letters:
            print(f'{letter[str(i)]}) {option}')
    print()

    while answer != 'A' and answer != 'B' and answer != 'C' and answer != 'D':

        try:
            answer = input('Answer the question: ').upper()

            if answer != 'A' and answer != 'B' and answer != 'C' and answer != 'D':

                print('ERRO: Digite a letra de uma das opções acima.')

            else:

                for i, option in enumerate(quest['Options']):

                    for letter in letters:

                        if letter[str(i)] == answer:

                            if quest['Answer'] == option:
                                correction = 'right'
                                hit += 1
                            else:
                                correction = 'wrong'
                                
                            answers.update({
                                f'Question {counter}' : [f'"{answer}) {option}"', correction]
                            })

        except:

            print('ERRO: Digite a letra de uma das opções acima.')


os.system('clear')
print(f'{name}, you got {hit} out of {counter} questions right.\n\nSee your answers:')

for key, value in answers.items():
    print(f"{key}: Your answer was {value[0]} and it's {value[1]}.")
    
if hit == counter:
    print('\nYou got all the answers right. Congratulations!')