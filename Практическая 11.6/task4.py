# Дано положительное действительное число X. 
# Выведите его первую цифру после десятичной точки. 
# При решении этой задачи нельзя пользоваться условной инструкцией, циклом или строками

x = float (input("Введите положительное действительное число X: "))
print(round((x * 10) % 10))


