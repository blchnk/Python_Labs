# Напишите скрипт, который читает текстовый файл и выводит символы
# в порядке убывания частоты встречаемости в тексте. Регистр символа
# не имеет значения. Программа должна учитывать только буквенные
# символы (символы пунктуации, цифры и служебные символы слудет
# игнорировать). Проверьте работу скрипта на нескольких файлах с
# текстом на английском и русском языках, сравните результаты с
# таблицами, приведенными в wikipedia.org/wiki/Letter_frequencies.

file = open('task1_lirics.txt', 'r')
text = file.read()
file.close()
vocabulary = {letter.lower(): text.count(letter) for letter in text if letter.isalpha()}
for value in sorted(vocabulary.keys(), key=vocabulary.get, reverse=True):
    print(value, ': ', vocabulary[value])

# file = open('task1_lirics.txt', 'r')
# text = file.read()
# text_alphaOnly = ''
# file.close()
# frequency = []
# symbol = []
#
# for i in range(len(text)):
#     if text[i].isalpha():
#         if text[i].isupper():
#             text_alphaOnly += text[i].lower()
#         else:
#             text_alphaOnly += text[i]
#
# for i in range(len(text_alphaOnly)):
#     if symbol.count(text_alphaOnly[i]) == 0:
#         frequency.append(text_alphaOnly.count(text_alphaOnly[i]))
#         symbol.append(text_alphaOnly[i])
# print(frequency)
# print(symbol)
#
# for i in range(len(symbol)):
#     k = frequency.index(max(frequency))
#     print('Символ: {0} встречается {1} раз(а)'.format(symbol[k], max(frequency)))
#     symbol.remove(symbol[k])
#     frequency.remove(frequency[k])