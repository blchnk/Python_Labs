# Напишите скрипт, позволяющий определить надежность вводимого
# пользователем пароля. Это задание является творческим: алгоритм
# определения надежности разработайте самостоятельно.

# Признаки надежного пароля:
# 1) Содержит более 8 символов                      [1-3]
# 2) Содержит буквы верхнего и нижнего регистров    [4-6]
# 3) Содержит символы (#, @, ~, ^)                  [7-9]
# 4) Содержит знаки препинания                      [10]

password = input('Введите пароль: ')
reliability_assessment = ['Слабый', 'Нормальный', 'Надежный', 'Очень надежный']
reliability_score = 0

if password is None:
    print('Вы ввели пустую строку!')
else:
    if len(password) > 8:
        reliability_score += 3
    if password.isupper() is False and password.islower() is False:
        reliability_score += 3
    if '#' in password or '@' in password or '~' in password or '^' in password:
        reliability_score += 3
    if ',' in password or '.' in password or '_' in password:
        reliability_score += 1

    if reliability_score <= 3:
        print(reliability_assessment[0])
    if 3 < reliability_score <= 6:
        print(reliability_assessment[1])
    if 6 < reliability_score <= 9:
        print(reliability_assessment[2])
    if reliability_score == 10:
        print(reliability_assessment[3])