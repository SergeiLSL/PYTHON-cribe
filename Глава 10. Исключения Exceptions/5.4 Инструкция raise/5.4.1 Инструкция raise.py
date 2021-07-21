"""
5.4 Инструкция raise

https://stepik.org/lesson/427822/step/1?unit=417707
"""
"""
При помощи инструкции raise можно возбуждать исключения в любой
строчке кода и при этом указывать сам тип исключения. Это могут
быть, как встроенные, так и свои самописные.
"""
try:
    1/0
except (KeyError, IndexError):
    print('LookupError')
except ZeroDivisionError:
    print('ZeroDivisionError')
