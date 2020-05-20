# Напишите параметризированный декоратор pre_process, который
# осуществляет предварительную обработку (цифровую фильтрацию)
# списка по алгоритму: s[i] = s[i]–a∙s[i–1]. Параметр а можно задать в
# коде (по умолчанию равен 0.97). Пример кода:
# @pre_process(a=0.93)
# def plot_signal(s):
#   for sample in s:
#     print(sample)


def pre_process(a):
    def decorator(func):
        def wrapper(*args):
            s = args[0]
            for i in range(len(s)):
                s[i] -= a * s[i-1]
                print('a =', a)
                func(s)
        return wrapper
    return decorator


@pre_process(a=0.97)
def pilot_signal(s):
    for sample in s:
        print(sample)


arr = [0, 1, 2, 3, 4, 5]
pilot_signal(arr)