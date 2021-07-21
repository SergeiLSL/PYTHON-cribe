"""
5.4 Инструкция raise

https://stepik.org/lesson/427822/step/1?unit=417707
"""
"""
Рассмотрим поподробней
"""

# try:
#     raise ValueError('Ошибка значения')
# except ValueError:
#     try:
#         raise TypeError('Ошибка типа')
#     except TypeError:
#         raise Exception('Большое исключение')

"""
Сейчас выводится выводе огромная информация об исключениях, 
но если мы не ходим все это выводить воспользуемся инструкцией from, 
которая выводит только последнее исключение.
"""

# print('*' * 30)
# try:
#     raise ValueError('Ошибка значения')
# except ValueError:
#     try:
#         raise TypeError('Ошибка типа')
#     except TypeError:
#         raise Exception('Большое исключение') from None  # Exception: Большое исключение

print('+' * 30)
"""
Поэкспериментируем. Мы каждому исключению дадим псевдоним.
"""

# try:
#     raise ValueError('Ошибка значения')
# except ValueError as first:
#     try:
#         raise TypeError('Ошибка типа')
#     except TypeError as second:
#         raise Exception('Большое исключение') from second  # Увидим все три исключения

print('+' * 30)
"""
Поэкспериментируем. Мы каждому исключению дадим псевдоним.
"""

try:
    raise ValueError('Ошибка значения')
except ValueError as first:
    try:
        raise TypeError('Ошибка типа')
    except TypeError as second:
        raise Exception('Большое исключение') from first  # Увидим два исключения,
        # TypeError проскакиваем, т.к. исключение вызваем из first

