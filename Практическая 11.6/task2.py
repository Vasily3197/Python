import math

# В одном аналитическом центре,
# где занимаются разного рода математическим анализом,
# работал практикант,
# который написал программу для расчёта некоторых функций.
# Правда, он в тот день очень устал
# и немного не так прочитал техническое задание 
# и функции теперь рассчитываются довольно грубо.
# 
# Вводится последовательность из N вещественных чисел.
# При этом положительные числа округляются вверх, отрицательные округляются вниз.
# 
# Напишите программу,
# которая выводит натуральный логарифм от числа,
# если оно положительное, и экспоненту в степени числа, если оно отрицательное или равно нулю.
# 
# Пример:
# 
# Введите кол-во чисел: 3
# Введите число: 1.3
# x = 2   log(x) = 0.6931471805599453

number_of_numbers = int (input("Ведите количество чисел: "))

for number_of_numbers in range (0,number_of_numbers):

    number = float (input("Ведите число: "))

    if (number > 0):
        log_x = math.ceil(number)
        print("x =", log_x, "\tlog(x) =", math.log(log_x))

    elif (number < 0):
        exp_x = math.floor(number)
        print("x =", exp_x, "\texp(x) =", math.exp(exp_x))

    else:
        print("0")