"""
5.3.1 Обработка исключений try-except

https://stepik.org/lesson/427821/step/1?unit=417706
"""
"""
Как же обрабатываются ошибки
"""

try:
    int('hello')  # ValueError: invalid literal for int() with base 10: 'hello'
    print('123')
    1/0  #
    a+b
except ValueError:  # Указываем какую ошибку хотим отловить
    print('error ValueError')  # ошибка ValueError

print('*' * 30)
"""
Выводится ошибка ValueError, но при этом обработалась, только первая строка
выводится сообщение и выполнение кода блокируется, как будто сработал break.
Усложним задачу.
"""
# try:
#     1/0  #
#     int('hello')  # ValueError: invalid literal for int() with base 10: 'hello'
#     print('123')
#     a+b
# except ValueError:  # Указываем какую ошибку хотим отловить
#     print('error ValueError')  # ошибка ZeroDivisionError: division by zero
"""
В данном слкчае наш блок реагирует на ситуацию ValueError,
а  ZeroDivisionError не может отловить.
Чтобы решить эту задачу можно добавить еще один  except.
"""
print('+' * 30)
try:
    1/0  #
    int('hello')  # ValueError: invalid literal for int() with base 10: 'hello'
    print('123')
    a+b
except ValueError:  # Указываем какую ошибку хотим отловить
    print('error ValueError')  # ошибка ZeroDivisionError: division by zero
except ZeroDivisionError:  # Указываем какую ошибку хотим отловить
    print('error ZeroDivisionError')  # ошибка ZeroDivisionError: division by zero

print('=' * 30)
"""
Но остальные строки по прежнему не выполняются.
уберем деление на ноль и в int добавим число. 
У нас появляется новая ошибка.
Обработаем её и у нас все прекрасно отработает.
"""
try:
    int('123456')  #
    print('123')
    a+b  # NameError: name 'a' is not defined
except ValueError:  # Указываем какую ошибку хотим отловить
    print('error ValueError')  # ошибка ZeroDivisionError: division by zero
except ZeroDivisionError:  # Указываем какую ошибку хотим отловить
    print('error ZeroDivisionError')  # ошибка ZeroDivisionError: division by zero
except NameError:  # Указываем какую ошибку хотим отловить
    print('error NameError')  # ошибка NameError: name 'a' is not defined

"""
В блок try можно добавлять сколько угодно исключений except, в котором 
указываете какое исключение хотите отловить, а затем, что-надо выполнить. 
"""