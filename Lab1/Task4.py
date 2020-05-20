# Напишите скрипт, который разделяет введенный с клавиатуры текст на
# слова и выводит сначала те слова, длина которых превосходит 7
# символов, затем слова размером от 4 до 7 символов, затем – все
# остальные.

text = input('Введите текст: ').split(' ')
[print(i) for i in text if len(i) > 7]
[print(i) for i in text if 3 < len(i) < 6]
[print(i) for i in text if len(i) <= 4]
# [print(i) for i in [print(i) if (i is not None and 3 < len(i) < 7)
#                     else i for i in [print(i) if (len(i) > 6) else i for i in text]] if i is not None and len(i) < 4]
