# Задание №1 
import math as mt
import random

# x = int(input('Введите х= '))

# if 1 <= x <= 2:
#     y = mt.pow(x,2) * mt.log10(x)

# elif x < 1:
#     y = 1 
# else:
#     mt.e(2*x) * mt.cos(5 * x)

# print(f'При х= {x}, y= {y}')


# Задание №2
a = []
summ = 0

for _ in range(10):
    a.append(random.randint(0, 10) - 5)

for i in a:
    if i > 0:
        summ +=i
print(f'Сумма положительных элементов списка \n{a}\nРезультат: {summ}')