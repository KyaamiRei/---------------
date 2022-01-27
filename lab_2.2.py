a = [11, 22, 33]

# try:
#     for i in range(5):
#         print(a[i])
# except IndexError:
#     print('Данного индекса в списке нет!')

try:
    print(a[5])
except Exception as err:
    print(err)