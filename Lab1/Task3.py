# Напишите скрипт, который позволяет ввести с клавиатуры номер
# дебетовой карты (16 цифр) и выводит номер в скрытом виде: первые и
# последние 4 цифры отображены нормально, а между ними – символы
# «*» (например, 5123 **** **** 1212).

# 0123 4567 8910 1234

credit_card = input('Введите номер кредитной карты: ').replace(' ', '')
print(credit_card[:4] + ' ' + '*'*4 + ' ' + '*'*4 + ' ' + credit_card[-4:]) \
    if len(credit_card) == 16 else print('Неверно введены данные!')
