"""
Мы сами вправе вызывать исключения
"""
# print('+' * 35)
#
# print('hello1')
# print('hello2')
# print('hello3')
# raise ValueError('Неправильное значение')
# print('hello5')

"""
Это полезно делать например в таких случаях
"""

try:
    a = int(input())  # вызывает ошибку KeyError
except:
    raise ValueError('Неправильное значение, передавайте число')  # в
    # таком случае пользователь видит не только тип ошибки на английском языке, но и на русском
print('hello5')
print('hello6')
