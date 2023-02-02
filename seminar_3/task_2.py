# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5


from random import randint
lst = []
count = 0
k = int(input('Введите длинну массива: '))
a = 0
x = int(input('Введите число которое будем искать: '))
for i in range(0, k):
    lst.append(randint(1, k))
print(lst)

for i in range(len(lst)):
    if x == lst[i]:
        a = lst[i]
        print(a)
        break
    elif x == lst[i] -1:
        a = lst[i]
        print(a)
        break
    elif x == lst[i] + 1:
        a = lst[i]
        print(a)
