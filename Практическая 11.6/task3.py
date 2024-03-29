# Вы пишете программу-инсталлятор для компьютерной игры.
# Пока инсталлятор скачивает обновление,
# пользователю нужно показать сколько процентов уже скачалось,
# чтобы он мог решить пойти заварить чаю, или подождать у экрана компьютера.
# 
# Обновления игры всегда занимают разное количество мегабайт,
# да и скорость интернет-соединения у игроков разная.
# 
# Напишите программу,
# принимающую на вход размер файла обновления в мегабайтах
# и скорость интернет соединения в мегабайтах в секунду.
# 
# Для каждой секунды программа рассчитывает
# и выводит на экран сколько процентов от всего объема уже скачано,
# до тех пор пока не будет скачан весь объем.
# В конце программа должна показать сколько всего секунд заняло скачивание обновления.
# Обеспечьте контроль ввода.
# 
# Пример:
# 
# Укажите размер файла для скачивания: 123
# Какова скорость вашего соединения? 27
# 
# Прошло 1 сек. Скачано 27 из 123 Мб (22%)
# Прошло 2 сек. Скачано 54 из 123 Мб (44%)
# Прошло 3 сек. Скачано 81 из 123 Мб (66%)
# Прошло 4 сек. Скачано 108 из 123 Мб (88%)
# Прошло 5 сек. Скачано 123 из 123 Мб (100%)

import math
import time

time_sec = 1
file_size = int (input("Укажите размер файла для скачивания: " ))
speed = int (input("Укажите скорость Вашего соединения: " ))
str_info = "Прошло {0} секунд. Скачано {1} Мб из {2} Мб ( {3}% )"

for mb in range(speed, file_size, speed):
    print(str_info.format(time_sec, mb, file_size, math.ceil (100 * mb / file_size)))
    time_sec += 1
    time.sleep(1)

else:
    print(str_info.format(time_sec, file_size, file_size, math.ceil(100 * file_size / file_size)))