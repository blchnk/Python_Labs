# Напишите программу, позволяющую ввести с клавиатуры текст
# предложения и вывести на консоль все символы, которые входят в этот
# текст ровно по одному разу.

text = input("Введите текст: ")
simbols = ""
while True:
    for i in range(len(text)):
        if text.count(text[i], 0, len(text.lower())) == 1:
            simbols += text[i]
    break

print(simbols)
