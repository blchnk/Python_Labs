# Напишите скрипт, который на основе списка из 16 названий
# футбольных команд случайным образом формирует 4 группы по 4
# команды, а также выводит на консоль календарь всех игр (игры
# должны проходить по средам, раз в 2 недели, начиная с 14 сентября
# текущего года). Даты игр необходимо выводить в формате «14/09/2016,
# 22:45». Используйте модули random и itertools.

import random
import datetime
import itertools

teams = ['Россия', 'Испания', 'Италия', 'Франция', 'Англия', 'Германия', 'Швеция', 'Дания',
         'Греция', 'Бельгия', 'Китай', 'Бразилия', 'Аргентина', 'Урлай', 'Турция', 'Португалия']
random.shuffle(teams)
teams = [teams[i*4:i*4+4] for i in range(0, 4)]
groups = [i for i in itertools.combinations(teams, 4)]
[print('Группа №', i+1, groups[0][i]) for i in range(0, 4)]

now = datetime.datetime.now()
start = datetime.datetime(now.year, 9, 14, 22, 45)
for i in range(1, 16):
    print('Игра №', i, start.strftime('%d/%m/%Y %H:%M'))
    start += datetime.timedelta(days=14)
