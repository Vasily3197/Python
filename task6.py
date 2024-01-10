# Семья из трёх человек устала тесниться в однушке и наконец решила переехать.
# При обсуждении,
# какую же всё-таки купить квартиру исходя из своих предпочтений и семейного бюджета,
# они остановились на нескольких вариантах:

# Первый вариант 
# они готовы взять квартиру попросторнее (не менее 100 квадратных метров),
# но стоимостью не более 10 млн.
 
# Второй вариант — немного расширить круг поиска,
# то есть взять квартиру поменьше (от 80 квадратный метров),
# но и стоимостью не более 7 млн.
 
# Напишите программу,
# которая получает на вход стоимость квартиры и её площадь
# и выводит сообщение о том, подходит она или нет

area = int(input("Введите площадь квартиры: "))
cost = int(input("Введите стоимость квартиры: "))

if (area >= 100 and cost <= 10000000) or (area >= 80 and cost <= 7000000):
    print("Квартира подходит!")
else:
    print("Квартира  не подходит!")
    