# Напишите робота для коллекторов.
# В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор, 
# пока он не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга сообщите об этом пользователю и поблагодарите его.
 
# Пример:
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50
 
# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.
 
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!

credit = 1000
name = input ('Как Ваше имя? ')
print(name, 'Ваша задолженность составляет', credit, '.')
money = int(input("Сколько Вы готовы внести, что бы её погасить? "))

if money == 1000:
    print("Отлично", name, "! Вы погасили долг. Спасибо!")
else:
    while money < credit:
        money = int(input('Этого мало. Сколько Вы готовы внести сейчас? '))
    print("Отлично", name, "! Вы погасили долг. Спасибо!")
    