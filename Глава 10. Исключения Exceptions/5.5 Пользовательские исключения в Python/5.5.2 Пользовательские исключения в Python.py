"""
5.5 Пользовательские исключения в Python

https://stepik.org/lesson/427823/step/1?unit=417708
"""
"""
Создадим свой (дочерний) класс MyException, а наследовать 
мы его будем от Exception
"""


class MyException(Exception):  # Это класс можно оставить вообще пустым,
    # но мы сделаем запись
    """this is my first Exception"""

    def __init__(self, *args):
        if args:
            self.message = args[0]  # будем сохранять первое значение
        else:
            self.message = None

    def __str__(self):
        print('str called')
        if self.message:
            return f'MyException ({self.message})'
        else:
            return f'MyException is empty'


raise MyException('hello', 1, 2)  # __main__.MyException: ('hello', 1, 2)



