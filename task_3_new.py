from itertools import zip_longest
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


spisok = (i for i in zip_longest(tutors, klasses))
print(next(spisok))
print(next(spisok))
print(next(spisok))
print(next(spisok))
print(next(spisok))
print(next(spisok))
print(next(spisok))
print(next(spisok))


#print(list(generator(tutors, klasses)))