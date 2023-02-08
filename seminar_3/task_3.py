# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

# Ввод:
# ноутбук
# Вывод:
# 12


# point_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
# point_2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
# point_3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
# point_4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
# point_5 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
# point_8 = ['J', 'X', 'Ш', 'Э', 'Ю']
# point_10 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']

# word = input('Введите слово: ')
# word = word.upper()
# word_lst = list(word)
# print(word_lst)
# for i in range(len(word_lst), len(point_1)):
# #     if word_lst[i] in point_1[i]:
# #         print(1)
# import re
# def cyrillus(text):
#     return bool(re.search('[а-яА-я]', text))
# text = str.upper(input('Введите слово: '))

# def fun(x):
#     for key in alf:
#         if x in key:
#             return alf.get(key)

# def fun_1(text):
#     for key in alf_2:
#         if text in key:
#             return alf_2.get(key)
            
# # if cyrillus(text):
# #     print(fun)
# # else:
# #     print(fun_1)


# alf = {
#     'АВЕИНОРСТ' : 1,
#     'ДКЛМПУ' : 2, 
#     'БГЁЬЯ' : 3,
#     'ЙЫ' : 4,
#     'ЖЗХЦЧ' : 5,
#     'ШЭЮ' : 8,
#     'ФЩЪ' : 10,
# }

# alf_2 = {
#     'AEIOULNSTR' : 1,
#     'DG' : 2,
#     'BCMP' : 3,
#     'FHVWY' : 4,
#     'K' : 5,
#     'JX' : 8,
#     'QZ' :10
#     }
# text = input('Введите слово: ')
# print(sum(map(fun_1, str(input('Введите слово: ')))))




# def fun(x):
#     for key in dct:
#         if x in key:
#             return dct.get(key)
 

# print(sum(map(fun, input())))

# cyrillus = {'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'}
# a = 0
# def has_cyrillus(text):
#     for i in text:
#         if i in cyrillus:
#             a = 1
#         else:
#             a = 2
    
    

# print(has_cyrillus, input('Введите слово: '))



# def fun(x):
#     for key in alf:
#         if x in key:
#             return alf.get(key)
#         else:
#             return alf_2.get(key)
# alf = {
#     'АВЕИНОРСТ' : 1,
#     'ДКЛМП' : 1, 
#     'БГЁЬЯ' : 3,
#     'ЙЫ' : 4,
#     'ЖЗХЦЧ' : 5,
#     'ШЭЮ' : 8,
#     'ФЩЪ' : 10,
# }
# a = input('Введите слово: ')

# for key in alf:
#     if x in key:
#         return alf.get(key)
#     else
# for i in alf


# alf = {
#     'АВЕИНОРСТ' : 1,
#     'ДКЛМП' : 1, 
#     'БГЁЬЯ' : 3,
#     'ЙЫ' : 4,
#     'ЖЗХЦЧ' : 5,
#     'ШЭЮ' : 8,
#     'ФЩЪ' : 10,
# }



import re
def isCyrillic(text):
	return bool(re.search('[а-яА-Я]', text))
points_en = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
points_ru = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
text = input('Введите слово: ').upper()
if isCyrillic(text):
	print(sum([k for i in text for k, v in points_ru.items() if i in v]))
else:
	print(sum([k for i in text for k, v in points_en.items() if i in v]))