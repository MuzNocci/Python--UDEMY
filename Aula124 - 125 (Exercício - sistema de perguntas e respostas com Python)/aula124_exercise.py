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

print('########################################')
print('Welcome to Math Test')
print('########################################\n')
name = input("What's your name? ")

i = 0
hit = 0
answers = {}

for quest in questions:
    i += 1
    print('\n########################################\n')
    print(f"{name}, {quest['Question'].lower()}")
    print(f"Choose between the options: {str(quest['Options']).replace('[', '').replace(']','')}")
    answer = input('Answer the question: ')
    if answer == quest['Answer']:
        correction = 'right'
        hit += 1
    else:
        correction = 'wrong'
    answers.update({
        f'Question {i}' : [answer, correction]
    })


print('\n########################################\n')
print(f'{name}, you got {hit} out of {i} questions right.\n\nSee your answers:')
for key, value in answers.items():
    print(f"{key}: Your answer was {value[0]} and it's {value[1]}.")
if hit == i:
    print('\nYou got all the answers right. Congratulations!')