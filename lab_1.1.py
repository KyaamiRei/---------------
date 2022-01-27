import math

def toFix(number):
    return '%.3f' % number

# x = int(input('x= '))

# a1 = math.cos(x) + math.sin(x) + math.cos(3*x) + math.sin(3*x)

# a2 = 1/4 - 1/4 * math.sin(5/2 * math.pi + 8 * x)

# print('a1= %.3f' % a1)
# print('a2= %.3f' % a2)

#Задание №2
r = int(input('Введите радиус сферы R= '))

s_sh = (4 * math.pi * math.pow(r,2))
v_sh = 4/3 * math.pi * math.pow(r,3)

print(f'Cфера с радиусом {r}\nПлощаль: {toFix(s_sh)}\nОбъем: {toFix(v_sh)}')

#Задание №3
