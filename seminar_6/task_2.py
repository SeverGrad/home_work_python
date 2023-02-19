# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)


# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint
randon_lst  = []
index_lst = []
for i in range(1, 20):
    randon_lst.append(randint(-20, 20))
print(randon_lst)

min_number = int(input('Введите минимум: '))
max_number = int(input('Введите максимум: '))

for i in range(len(randon_lst)):
    if max_number >= randon_lst[i] and min_number <= randon_lst[i]:
        index_lst.append(i)
print(index_lst)
