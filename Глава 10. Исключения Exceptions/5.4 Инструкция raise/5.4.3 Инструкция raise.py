"""
5.4 Инструкция raise

https://stepik.org/lesson/427822/step/1?unit=417707
"""
"""
Где нам это понадобится?
"""
#
# try:
#     [1, 2, 3][8]
# except (KeyError, IndexError) as error:  # можно добавить несколько исключений
#     print(f'fLogging error: {repr(error)}')  # fLogging error: IndexError('list index out of range')
#     raise
# except ZeroDivisionError as err:
#     print('error ZeroDivisionError')
#     print(f'fLogging error {err} {repr(err)}')

"""
В raise можно добавить 
"""
print('*' * 30)

# try:
#     [1, 2, 3][8]
# except (KeyError, IndexError) as error:  # можно добавить несколько исключений
#     print(f'fLogging error: {repr(error)}')  # fLogging error: IndexError('list index out of range')
#     raise error
# except ZeroDivisionError as err:
#     print('error ZeroDivisionError')
#     print(f'fLogging error {err} {repr(err)}')


print('*' * 30)
"""
Что произойдет если будем делать исключения (KeyError, IndexError), 
а raise будем делать для TypeError
"""
try:
    [1, 2, 3][8]
except (KeyError, IndexError) as error:  # можно добавить несколько исключений
    print(f'fLogging error: {repr(error)}')  # fLogging error: IndexError('list index out of range')
    raise TypeError('Ошибка типа')
except ZeroDivisionError as err:
    print('error ZeroDivisionError')
    print(f'fLogging error {err} {repr(err)}')