"""
Переменные и типы данных
"""
"""
Переменная хранит определенные данные. Название переменной в Python 
должно начинаться с алфавитного символа или со знака подчеркивания и 
может содержать алфавитно-цифровые символы и знак подчеркивания. 
И кроме того, название переменной не должно совпадать с названием 
ключевых слов языка Python. Ключевых слов не так много, их легко 
запомнить: 
and, as, assert, break, class, continue, def, del, elif, else, except, 
False, finally, for, from, global, if, import, in, is, lambda, None, 
nonlocal, not, or, pass, raise, return, True, try, while, with, yield.
"""
"""
Например, создадим переменную:
"""
name = "Tom"
"""
Здесь определена переменная name, которая хранит строку "Tom".

В пайтоне применяется два типа наименования переменных: 
camel case и underscore notation.

Camel case подразумевает, что каждое новое подслово в наименовании 
переменной начинается с большой буквы. Например:
"""
userName = "Tom"
"""
Underscore notation подразумевает, что подслова в наименовании 
переменной разделяются знаком подчеркивания. Например:
"""
user_name = "Tom"
"""
И также надо учитывать регистрозависимость, поэтому переменные name и Name 
будут представлять разные объекты.

Переменная хранит данные одного из типов данных. 
В Python существует множество различных типов данных, 
которые подразделяются на категории: числа, последовательности, словари, наборы:

boolean - логическое значение True или False

int - представляет целое число, например, 1, 4, 8, 50.

float - представляет число с плавающей точкой, например, 1.2 или 34.76

complex - комплексные числа

str - строки, например "hello". В Python 3.x строки представляют набор символов в кодировке Unicode

bytes - последовательность чисел в диапазоне 0-255

byte array - массив байтов, аналогичен bytes с тем отличием, что может изменяться

list - список

tuple - кортеж

set - неупорядоченная коллекция уникальных объектов

frozen set - то же самое, что и set, только не может изменяться (immutable)

dict - словарь, где каждый элемент имеет ключ и значение
"""
"""
Python является языком с динамической типизацией. Он определяет тип данных 
переменной исходя из значения, которое ей присвоено. Так, при присвоении строки 
в двойных или одинарных кавычках переменная имеет тип str. 
При присвоении целого числа Python автоматически определяет тип переменной 
как int. Чтобы определить переменную как объект float, ей присваивается 
дробное число, в котором разделителем целой и дробной части является точка. 
Число с плавающей точкой можно определять в экспоненциальной записи:
"""
x = 3.9e3
print(x)  # 3900.0

x = 3.9e-3
print(x)  # 0.0039

"""
Число float может иметь только 18 значимых симолов. Так, в данном случае 
используются только два символа - 3.9. И если число слишком велико или слишком мало, 
то мы можем записывать число в подобной нотации, используя экспоненту. 
Число после экспоненты указывает степень числа 10, на которое надо умножить 
основное число - 3.9.

При этом в процессе работы программы мы можем изменить тип переменной, присвоив 
ей значение другого типа:
"""
user_id = "12tomsmith438"  # тип str
print(user_id)

user_id = 234  # тип int
print(user_id)

"""
С помощью функции type() динамически можно узнать текущий тип переменной:
"""
user_id = "12tomsmith438"
print(type(user_id))  # <class 'str'>

user_id = 234
print(type(user_id))  # <class 'int'>

