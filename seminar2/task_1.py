# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
from random import randint
coins = int(input('Введите количество монеток лежащих на столе: '))
eagle = 0
tails = 0
i = 0
lst_coins = []
while i < coins:
    lst_coins.append(randint(0,1))
    i += 1
print(lst_coins)


for v in range( len(lst_coins)):
    if lst_coins[v] == 0:
        eagle += 1
    else:
        tails +=1


if eagle > tails:
    print(tails)
else:
    print(eagle)





