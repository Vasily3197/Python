
# Напишите программу, которая считывает с клавиатуры три числа a, b и c, 
# считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.

c = int(input("Enter c: "))
summ = 0
count = 0

if c == 0:
    print("The solution is not possible")
else:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    for result in range (a, b+1):

        if result %c == 0:
            count += 1
            summ += result
    print(summ/count)