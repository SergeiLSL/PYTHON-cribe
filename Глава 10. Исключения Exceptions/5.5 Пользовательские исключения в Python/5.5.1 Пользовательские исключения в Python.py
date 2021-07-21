"""
5.5 Пользовательские исключения в Python

https://stepik.org/lesson/427823/step/1?unit=417708
"""
"""
Создадим свой (дочерний) класс MyException, а наследовать 
мы его будем от Exception
"""


# class MyException(Exception):  # Этот класс можно оставить вообще пустым, но мы сделаем запись
#     """this is my first Exception"""
#
#
# raise MyException  # __main__.MyException

"""
Также можно передавать какие то атрибуты
"""


# class MyException(Exception):  # Этот класс можно оставить вообще пустым, но мы сделаем запись
#     """this is my first Exception"""
#
#
# raise MyException('hello', 1, 2)  # __main__.MyException: ('hello', 1, 2)


"""
Теперь можно обрабатывать
"""


class MyException(Exception):  # # Этот класс можно оставить вообще пустым, но мы сделаем запись
    """this is my first Exception"""

try:
    raise MyException('hello', 1, 2)  # __main__.MyException: ('hello', 1, 2)
except MyException:
    print('done')  # обработано

