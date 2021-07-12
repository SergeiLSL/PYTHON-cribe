"""
Модуль math
- math включает в себя множество полезных математических функций,
    которые могут понадобиться при расчетах или построении моделей.
    Полный список функций представлен в документации:
    https://docs.python.org/3/library/math.html

Также существует версия на русском, но не на официальном сайте:
 https://pythonworld.ru/moduli/modul-math.html
Обращаясь к документации, решите следующие задачи:
Задача “Формула №1”
Задача “Формула №2”
"""
import math
# Константа, обозначающая число π
print(math.pi)  # 3.141592653589793
# Возвращает целую и дробную части числа
print(math.modf(15.689))  # (0.6890000000000001, 15.0)
# Возвращает x^y
print(math.pow(2, 3))  # 8.0
# Вычисляет корень из числа x
print(math.sqrt(64))  # 8.0
# Возвращает значение выражения e^x
print(math.exp(4))  # 54.598150033144236
# Вычисляет значение sin(x)
print(math.sin(60))  # -0.9880316240928618
# Округление вниз
print(math.floor(15.456))  # 15
# Округление вверх
print(math.ceil(15.456))  # 16
# Возвращает значение x!
print(math.factorial(6))  # 720
# Вычисляет логарифм x по основанию 2
print(math.log2(15))  # 3.9068905956085187



