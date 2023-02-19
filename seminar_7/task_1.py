# # Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# # разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# # стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# # гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# # слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# # от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# # напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# # в порядке

# Ввод:                                      Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам     Парам пам-пам
def sum_vowels(words):
    count = 0
    vowels = set('аоуэыяёюеи')
    for i in words:
        if i in vowels:
            count += 1
    return count


phrase = str(input('Введите фразу Винни-Пуха: '))
phrase_lst = phrase.lower().split()
# print(phrase_lst)
# print(sum_vowels(phrase_lst[1]))
t = sum_vowels(phrase_lst[0])
if all([sum_vowels(i) == t for i in phrase_lst]):
    print('пара-ра-рам рам-пам-папам па-ра-па-дам')
else:
    print('Парам пам-пам')