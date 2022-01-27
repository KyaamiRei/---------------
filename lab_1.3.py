import math as mt
import random 

def toFix(number):
    return '%.3f' % number

# Задание №1
# a = int(input('Введите первое граничение а= '))
# b = int(input('Введите второе граничение b= '))
# h = int(input('Введите шаг h= '))

# y_res = []

# for i in range(a,b):
#     y_res.append(mt.cos(i)/mt.sin(i))

# max = 0.0

# for i in y_res:
#     if float(i) > max:
#         max = i

# print(f'список результатов функции на промежутке {a},{b}\n{y_res}\nМаксимальное значение: {toFix(max)}')

# Задание №2
# temp = []
# count = 0

# for _ in range(10):
#     temp.append(random.randint(0, 10) - 5)

# for i in temp:
#     if i < 0:
#         count +=1
# print(f'Список температур:\n{temp}\nКол-во отрицательных температур: {count}')