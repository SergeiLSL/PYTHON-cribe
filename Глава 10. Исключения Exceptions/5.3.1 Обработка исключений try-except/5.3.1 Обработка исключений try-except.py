"""
5.3.1 Обработка исключений try-except

https://stepik.org/lesson/427821/step/1?unit=417706
"""

# 1/0  # ZeroDivisionError: division by zero - строчки ниже не выполняются
# a+b
# int('hello')

"""
Если поменяем порядок, то выполнится первая строка и вторую ошибку мы не увидим
"""
# int('hello')  # ValueError: invalid literal for int() with base 10: 'hello'
# 1/0  #
# a+b
