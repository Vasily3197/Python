print('Задача 4. Число наоборот')

# Вводится последовательность чисел,
# которая оканчивается нулём.
#
# Реализуйте функцию,
# которая принимает в качестве аргумента каждое число,
# переворачивает его и выводит на экран.

# Пример:
# Введите число: 1234
# Число наоборот: 4321
# 
# Введите число: 1000
# Число наоборот: 0001
# 
# Введите число: 0
# Программа завершена!
# 
# Дополнительно: добейтесь такого вывода чисел, если в его начале идут нули.
# 
# Введите число: 1230
# Число наоборот: 321
# 
# Кстати, нули, которые мы убрали, называются ведущими.

def reverse(number):

    if number > 0:
        reverse_number = 0
        while 0 < number:
                reverse_number = reverse_number * 10 + number % 10
                number //= 10

        return reverse_number
    else:
         print("Программа завершена!")

number = reverse(int(input("Введите число: ")))

print(f"Число наоборот: {number}")



  









