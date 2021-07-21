"""
5.3.1 Обработка исключений try-except

https://stepik.org/lesson/427821/step/1?unit=417706
"""

print('=' * 30)
"""
В блок try можно добавлять сколько угодно исключений except, в котором 
указываете какое исключение хотите отловить, а затем, что-надо выполнить. 
"""
"""
Если изменим прорграмму увидим новую ошибку IndexError: string index out of range.
Разберем все способы ее отловить
"""
s = 'hello'

try:
    s[6]
except IndexError:  # Указываем какую ошибку хотим отловить
    print('error IndexError')  # ошибка IndexError: string index out of range

print('=' * 30)
"""
Если мы вспомним иеархию, то увидим, что IndexError является дочерним классом
LookupError. Мы прекрасно сможем обработать ошибку этим способом.
"""

s = 'hello'

try:
    s[6]
except LookupError:  # Указываем какую ошибку хотим отловить
    print('error LookupError')  # ошибка error LookupError

print('=' * 30)
"""
Но при таком написании кода будут попадать и другие ошибки типа
IndexError и KeyError.
Можно в этом убедится, если вставить еще один блок и по аналогии
if elif первым будет исключение KeyError, дальше break/
"""

s = 'hello'
d = {}

try:
    d['key']
except KeyError:  # Указываем какую ошибку хотим отловить
    print('error KeyError')  # ошибка error error KeyError
except LookupError:  # Указываем какую ошибку хотим отловить
    print('error LookupError')  # ошибка error LookupError

print('=' * 30)

"""
Если блоки поменять местами первым будет исключение LookupError, 
так как в него входит KeyError и IndexError, дальше break.
"""

s = 'hello'
d = {}

try:
    d['key']
except LookupError:  # Указываем какую ошибку хотим отловить
    print('error LookupError')  # ошибка error LookupError
except KeyError:  # Указываем какую ошибку хотим отловить
    print('error KeyError')  # ошибка error error KeyError

print('=' * 30)

"""
Если удалить все исключения.
"""

s = 'hello'
d = {}

try:
    d['key']
except:  # Сюда пойдут все исключения, которые могут быть
    print('error')  # error

print('*' * 30)

"""
Если не помните все исключения или не ходите, 
тогда надо писать родительский класс (желательно-обязательно).
Ниже пример
"""
s = 'hello'
d = {}

try:
    1 + 'key'
except Exception:  # Сюда пойдут все исключения, которые могут быть
    print('error')  # error

print('=' * 30)
