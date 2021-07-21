"""
5.3.1 Обработка исключений try-except

https://stepik.org/lesson/427821/step/1?unit=417706
"""

"""
Разберем еще один блок - else, который тоже указывается один раз.
Использование просто finally и else не допускается, обязательно
должен быть хотябы один except.
"""

s = 'hello'
d = {}
# f = open('123.txt')

try:
    1/0

except (KeyError, IndexError):  # можно добавить несколько исключений
    print('LoockupError')
except ZeroDivisionError:
    print('error ZeroDivisionError')
else:
    print('good')  # этот блок отрабатывает только в том случае,
    # когда в try нет исключений. в противном случае получим ошибку
    # и в else не попадем
finally:
    print('end')  # этот блок выполняется всегда, независимо
    # f.close()

"""
Итоги:
try - можно использовать со множеством except. 
Как правило рекомендуется указывать тип исключения, который вы отлавливаете.
Также могут быть блоки else и finally.

Если except вам не нужны, то допускается исрользование try
таким образом (только try и finally: 
try:
    1/0
finally:
    print('end') 
 
Можно использовать только try и except, без else и finally.
"""
print('*' * 25)
"""
Исключениям можно давать имена и которые можно использовать
"""
try:
    {}['k']
except (KeyError, IndexError) as error:  # можно добавить несколько исключений
    print('LoockupError')
    print(f'fLogging error: {repr(error)}')  # fLogging error: KeyError('k') нет такого ключа в словаре
except ZeroDivisionError as err:
    print('error ZeroDivisionError')
    print(f'fLogging error {err} {repr(err)}')

print('+' * 25)
"""
Исключениям можно давать имена и которые можно использовать
"""
try:
    [1, 2, 3][8]
except (KeyError, IndexError) as error:  # можно добавить несколько исключений
    print('LoockupError')
    print(f'fLogging error: {repr(error)}')  # fLogging error: IndexError('list index out of range')
except ZeroDivisionError as err:
    print('error ZeroDivisionError')
    print(f'fLogging error {err} {repr(err)}')
