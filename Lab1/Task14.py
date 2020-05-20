# Напишите декоратор non_empty, который дополнительно проверяет
# списковый результат любой функции: если в нем содержатся пустые
# строки или значение None, то они удаляются. Пример кода:
# @non_empty
# def get_pages():
#   return ['chapter1', '', 'contents', '', 'line1']


def non_empty(func):
    def wrapper():
        return list(filter(None, func()))
    return wrapper


@non_empty
def get_pages():
    return ['chapter1', 0, 'contents', '', 'line1']


print(get_pages())
