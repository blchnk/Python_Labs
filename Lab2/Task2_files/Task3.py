# Задан путь к директории с музыкальными файлами (в названии
# которых нет номеров, а только названия песен) и текстовый файл,
# хранящий полный список песен с номерами и названиями в виде строк
# формата «01. Freefall [6:12]». Напишите скрипт, который корректирует
# имена файлов в директории на основе текста списка песен.

from pathlib import Path

path = Path(r'C:\Users\Admin\PycharmProjects\Lab2')
mask = '*.mp3'
playlist = Path(r'C:\Users\Admin\PycharmProjects\Lab2\playlist.txt')

cfg = {}
with playlist.open(encoding='utf-8') as f:
    for line in f:
        s = line.split('[')[0]
        cfg[s.split('.')[1].strip()] = s.strip()

for f in path.glob(mask):
    name = f.name.replace(f.suffix, '')
    f.rename(str(str(f).replace(name, cfg.get(name))))
