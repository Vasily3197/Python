print('Задача 6. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел

import math

def gcd (first, second): 
    
    while first != 0 and second != 0:

        if first > second: first = first % second
       
        else:  second = second % first
    
first = int (input("Введите первое число: "))
second = int (input("Введите второе число: "))

print(math.gcd(first, second))