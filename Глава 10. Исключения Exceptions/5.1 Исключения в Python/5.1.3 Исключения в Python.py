"""
5.1 Исключения в Python

https://stepik.org/lesson/427819/step/1?unit=417704
"""
"""
Давайте научимся отлавливать исключения и обрабатывать их
https://habr.com/ru/post/186608/
https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
https://younglinux.info/python/exceptions
"""

"""
Каждого класса мы можем создать свой экземпляр.
Например: Создадим экземпляр класса IndexError
"""
t = IndexError()
print(isinstance(t, IndexError))  # True в консоле пишет
print(isinstance(t, LookupError))  # True в консоле пишет
print(isinstance(t, TypeError))  # False в консоле пишет
print(isinstance(t, Exception))  # True  в консоле пишет

print('=' * 35)

print('hello1')
print('hello2')
print('hello3')
try:
    [1, 2][5]  # вызывает ошибку IndexError
except IndexError:
    print('Неправильный индекс')  # Неправильный индекс
print('hello5')
print('hello6')

print('*' * 35)

print('hello1')
print('hello2')
print('hello3')
try:
    [1, 2][5]  # вызывает ошибку LookupError
except LookupError:  # можно обратиться к родителю и этот код тоже будет работать
    print('Неправильный индекс')  # Неправильный индекс
print('hello5')
print('hello6')
""" 
Но при таком варианте мы будем отлавливать также ошибки которые относятся к KeyError
"""
print('*' * 35)

print('hello1')
print('hello2')
print('hello3')
try:
    {1: 2, 2: 6}[5]  # вызывает ошибку KeyError
except LookupError:  # можно обратиться к родителю и этот код тоже будет работать
    print('Неправильный индекс')  # Неправильный индекс
print('hello5')
print('hello6')

""" 
Если мы поставим LookupError, то мы будем отлавливать также ошибки которые 
относятся и к KeyError и  к IndexError
"""

