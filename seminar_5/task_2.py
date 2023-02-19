# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4


def sum(num_1, num_2):
    if num_1 == 0:
        return num_2
    return sum(num_1 - 1, num_2 + 1)


num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
print(sum(num_1, num_2))