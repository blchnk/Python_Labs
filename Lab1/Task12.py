# Напишите генератор get_frames(), который производит «оконную
# декомпозицию» сигнала: на основе входного списка генерирует набор
# списков – перекрывающихся отдельных фрагментов сигнала размера
# size со степенью перекрытия overlap. Пример вызова:
# for frame in get_frames(signal, size=2, overlap=0.5):
#   print(frame)

def get_frames(signal, size, overlap):
    step = int(size * overlap)
    start = 0
    while start < len(signal) - 1:
        yield signal[start: start + size]
        start += step


signal = [i for i in range(10)]
print('Сигнал: ' + str(signal))
for frame in get_frames(signal, 2, 0.5):
    print(frame)
