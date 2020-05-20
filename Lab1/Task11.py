# Напишите генератор frange как аналог range() с дробным шагом.
# Пример вызова:
# for x in frange(1, 5, 0.1):
#   print(x)
#   выводит 1 1.1 1.2 1.3 1.4 … 4.9

def frange(begin, end, step):
    while begin < end:
        yield round(begin, 1)
        begin += step


for x in frange(1, 5, 0.1):
    print(x, end="   ")  # Вывод без перехода на новую строку
