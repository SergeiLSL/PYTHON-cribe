""" Операции сравнения """

"""
Ряд операций представляют условные выражения. Все эти операции принимают 
два операнда и возвращают логическое значение, которое в Python 
представляет тип boolean. 
Существует только два логических значения:
 - True (выражение истинно) 
 - False (выражение ложно).
"""

"""
Простейшие условные выражения представляют операции сравнения, 
которые сравнивают два значения. Python поддерживает следующие 
операции сравнения:

==
Возвращает True, если оба операнда равны. Иначе возвращает False.

!=
Возвращает True, если оба операнда НЕ равны. Иначе возвращает False.

> (больше чем)
Возвращает True, если первый операнд больше второго.

< (меньше чем)
Возвращает True, если первый операнд меньше второго.

>= (больше или равно)
Возвращает True, если первый операнд больше или равен второму.

<= (меньше или равно)
Возвращает True, если первый операнд меньше или равен второму.

Примеры операций сравнения:
"""
a = 5
b = 6
result = 5 == 6  # сохраняем результат операции в переменную
print(result)  # False - 5 не равно 6
print(a != b)  # True
print(a > b)  # False - 5 меньше 6
print(a < b)  # True

bool1 = True
bool2 = False
print(bool1 == bool2)  # False - bool1 не равно bool2

"""
Операции сравнения могут сравнивать различные объекты - строки, 
числа, логические значения, однако оба операнда операции должны 
представлять один и тот же тип.
"""
