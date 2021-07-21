"""
5.4 Инструкция raise

https://stepik.org/lesson/427822/step/1?unit=417707
"""
"""
При помощи инструкции raise можно возбуждать исключения в любой
строчке кода и при этом указывать сам тип исключения. Это могут
быть, как встроенные, так и свои самописные.
"""
"""
Под exception понимается либо встроенный класс ошибки, либо
isinstance()
В raise можно писать только классы исключения
"""

# raise Exception('Big error', 1, 2)  # Exception: ('Big error', 1, 2)
# # Все что укажим будет указываться при инициализации класса

# try:
#     [1, 2, 3][8]
# except (KeyError, IndexError) as error:  # можно добавить несколько исключений
#     print('LoockupError')
#     print(f'fLogging error: {repr(error)}')  # fLogging error: IndexError('list index out of range')
# except ZeroDivisionError as err:
#     print('error ZeroDivisionError')
#     print(f'fLogging error {err} {repr(err)}')

print('*' * 30)
"""
Можно создать переменную, а потом вызывать исключения
"""

er = Exception('Big error')
raise er  # Exception: Big error
# Все что укажим будет указываться при инициализации класса

try:
    [1, 2, 3][8]
except (KeyError, IndexError) as error:  # можно добавить несколько исключений
    print('LoockupError')
    print(f'fLogging error: {repr(error)}')  # fLogging error: IndexError('list index out of range')
except ZeroDivisionError as err:
    print('error ZeroDivisionError')
    print(f'fLogging error {err} {repr(err)}')