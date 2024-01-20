# -*- coding: utf-8 -*import

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. 

number_of_numbers = int(input("Введите количество чисел: "))

max_sum = 0
max_digit = 0

for _ in range(number_of_numbers):
    num = int(input("Введите число: "))
    summ = sum(int(digit) for digit in str(num))
    
    if summ > max_sum:
        max_sum = summ
        max_digit = num

print(f"Наибольшее число {max_digit}. Сумма его цифр составляет: {max_sum}")

