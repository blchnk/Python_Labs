# Напишите скрипт, который преобразует введенное с клавиатуры
# вещественное число в денежный формат. Например, число 12,5 должно
# быть преобразовано к виду «12 руб. 50 коп.». В случае ввода
# отрицательного числа выдайте сообщение «Некорректный формат!»
# путем обработки исключения в коде.

try:
    [print(int(i//1),"рублей",round((i-i//1)*100),"копеек") if i>= 0 else print(0/0) for i in [float(input("Ввод: "))]]
except ZeroDivisionError:
    print("Некоректный формат")
