import random

puzzles = {'Загадка 1': 'Ответ1',
           'Загадка 2': 'Ответ2',
           'Загадка 3': 'Ответ3',
           'Загадка 4': 'Ответ4',
           'Загадка 5': 'Ответ5'
           }

s_key = [*puzzles]
print(s_key)
r = random.choice(s_key)
print(r)
