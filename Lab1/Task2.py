# Написать скрипт, который выводит на экран «True», если элементы
# программно задаваемого списка представляют собой возрастающую
# последовательность, иначе – «False».

print('Введите три числа: ')
numbers = [input() for i in range(0, 3)]


def check(arr):
    for i in range(1, len(arr) - 1):
        if numbers[i] < numbers[i - 1]:
            return False
    return True


print(check(numbers))
print(numbers)
