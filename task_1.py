"""
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
odd_to_15 = odd_nums(15)
next(odd_to_15)
2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""
def odd_nums(max):
    for nam in range(1, max + 1):
        if nam % 2 == 1:
            yield nam

def odd_numsets(num):
     return range(1, num + 1, 2)



odd_numset = (i for i in range(1, 15 + 1, 2 ))


odd_to_17 = odd_numsets(17)
print(list(odd_to_17))
#print(next(odd_numset))
#print(next(odd_numset))
#print(next(odd_numset))
#print(next(odd_numset))
#print(next(odd_numset))
#print(next(odd_numset))
#print(next(odd_numset))
#print(next(odd_numset))
#odd_to_15 = odd_nums(15)
#print(next(odd_to_15))
#print(next(odd_to_15))
#print(next(odd_to_15))
#print(next(odd_to_15))
#print(next(odd_to_15))
#print(next(odd_to_15))
#print(next(odd_to_15))
#print(next(odd_to_15))
