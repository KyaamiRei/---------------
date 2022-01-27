# Задания №1
# f = open("result.txt", "w", encoding="utf-8")

# while True:
#     str = input('Введите строку: ')
#     if str != "":
#         f.write(str + '\n')
#     else:
#         print('Ввод завершен!')
#         break

# f.close()

# Задание №2
f = open("result.txt", "r")

count_line = 0



for i in f:
    count_line += 1
    
    print(f'Строка {count_line}, кол-во букв: {len(i)}')

f.close()