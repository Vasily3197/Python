import random
# Задача 4. Успеваемость в классе

# Что нужно сделать
# В классе N человек. Каждый из них получил за урок по информатике оценку: 
# 3, 4 или 5, двоек сегодня не было. Напишите программу, которая получает список оценок — N чисел — и выводит 
# на экран сообщение о том, кого сегодня больше: отличников, хорошистов или троечников.

# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.

# Что оценивается
# Задание считается успешно выполненным, если:

# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# в выводе присутствует сообщение о том, кого больше;
# для решения используется цикл for, а не встроенные функции или рекурсия;
# переменные имеют значащие имена, не только a, b, c, d.

people = int (input("Введите количество человек в классе: "))

for journal in range(1, people + 1):   
    journal = random.randint(3,5)  
    print(journal) 
if journal > 4 > 3:
    print("Сегодня больше пятёрок")
elif journal < 4 < 5:
    print("Сегодня больше троек")
else:
    print("Сегодня больше четвёрок")

     
     


    

    

    
    
    




