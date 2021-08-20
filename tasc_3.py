"""
3. Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
('Станислав', None)
"""
from itertools import zip_longest
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
def list_school():
    for name, klass in zip_longest(tutors, klasses, fillvalue=None):
        yield name, klass

school_list = list_school()
print(next(school_list))
print(next(school_list))
print(next(school_list))
print(next(school_list))
print(next(school_list))
print(next(school_list))
print(next(school_list))
print(next(school_list))

#spisok = (name, klass for name, klass in zip_longest(tutors,klasses, fillvalue=None))
#print(next(spisok))
