#  Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12



num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
lst_num_1 = []
lst_num_2 = []

while len(lst_num_1) < num_1:
    lst_num_1.append(int(input('Введите число:')))
print(lst_num_1)


while len(lst_num_2) < num_2:
    lst_num_2.append(int(input('Введите число:')))
print(lst_num_2)

set_num_1 = set(lst_num_1)
set_num_2 = set(lst_num_2)
set_num_perecesh = set_num_1.intersection(set_num_2)
# lst_1 = list(set_num_perecesh)
print(set_num_perecesh)
print(sorted(set_num_perecesh))


