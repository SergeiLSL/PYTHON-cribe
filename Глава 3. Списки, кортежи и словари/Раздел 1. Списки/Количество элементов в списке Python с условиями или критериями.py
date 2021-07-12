"""
Количество элементов в списке Python с условиями или критериями.

https://pythonru.com/primery/kolichestvo-elementov-v-spiske-python
"""
"""
В этом посте мы рассмотрим, как узнать число элементов в списке Python, 
удовлетворяющих определенным условиям или критериям.

Если вам просто нужно найти количество конкретных элементов с списке, 
используйте метод .count()
"""
list_numbers = [1, 2, 2, 5, 5, 7, 4, 2, 1]
print(list_numbers.count(2))  # 3
"""
Существует несколько способов такого подсчета, и мы изучим каждый из них 
с помощью примеров. Итак, давайте начнем.

1. Использование цикла for для подсчета в списке Python
В этом фрагменте кода мы используем цикл for для подсчета элементов списка 
Python, удовлетворяющих условиям или критериям. 
Мы перебираем каждый элемент списка и проверяем условие, если оно истинно, 
то мы увеличиваем счетчик на 1. Это простой процесс сопоставления и подсчета 
для получения интересующего нас количества.
"""
list_numbers = [78, 99, 66, 44, 50, 30, 45, 15, 25, 20]
count = 0

for item in list_numbers:
    if item % 5 == 0:
        count += 1

print("количество элементов списка, удовлетворяющих заданному условию:", count)
"""
количество элементов списка, удовлетворяющих заданному условию: 6

2. Применение len() со списковыми включениями для подсчета в списке Python
В представленном ниже фрагменте кода, мы используем списковые включения 
(list comprehension), чтобы создать новый список, элементы которого 
соответствует заданному условию, после чего мы получаем длину собранного списка. 
Это намного легче понять на примере, поэтому давайте перейдем к нему.
"""
list_numbers = [78, 99, 66, 44, 50, 30, 45, 15, 25, 20]
element_count = len([item for item in list_numbers if item%5 == 0])

print("количество элементов списка, удовлетворяющих заданному условию:", element_count)
"""
количество элементов списка, удовлетворяющих заданному условию: 6

Подсчет ненулевых элементов
В этом примере мы находим общее количество ненулевых элементов. 
Чтобы узнать число нулевых членов списка, мы можем просто изменить 
условие на if item == 0.
"""
list_numbers = [78, 99, 66, 44, 50, 30, 45, 0, 0, 0]
element_count = len([item for item in list_numbers if item != 0])

print("количество элементов списка, удовлетворяющих заданному условию:", element_count)
"""
количество элементов списка, удовлетворяющих заданному условию: 7

3. sum() и выражение-генератор для подсчета в списке Python
В этом примере кода мы используем sum() с генераторным выражением. 
Каждый элемент списка проходит проверку условием и для тех элементов, 
которые ему удовлетворяют, возвращается значение True. 
Метод sum() в свою очередь подсчитывает общее число истинных значений.
"""
list_numbers = [78, 99, 66, 44, 50, 30, 45, 15, 25, 20]
count = 0
count = sum(True for i in list_numbers if i % 5 == 0)

print("количество элементов списка, удовлетворяющих заданному условию:", count)
"""
количество элементов списка, удовлетворяющих заданному условию: 6

4. sum() и map() для подсчета элементов списка Python с условиями или критериями
Функция map(fun, iterable) принимает два аргумента: итерируемый объект 
(это может быть строка, кортеж, список или словарь) и функцию, которая 
применяется к каждому его элементу, — и возвращает map-объект (итератор). 
Для применения одной функции внутри другой идеально подходит лямбда-функция. 
Таким образом, map() примет первый аргумент в виде лямбда-функции.

Здесь sum() используется с функцией map(), чтобы получить количество 
всех элементов списка, которые делятся на 5.

Давайте разберемся на примере, в котором переданная лямбда-функция 
предназначена для фильтрации членов списка, не кратных 5.
"""
list_numbers = [78, 99, 66, 44, 50, 30, 45, 15, 25, 20]
count = 0
count = sum(map(lambda item: item % 5 == 0, list_numbers))

print("количество элементов списка, удовлетворяющих заданному условию:", count)
"""
количество элементов списка, удовлетворяющих заданному условию: 6

5. reduce() с лямбда-функцией для подсчета элементов списка Python 
с условием или критериями
Lambda — это анонимная (без имени) функция, которая может принимать 
много параметров, но тело функции должно содержать только одно выражение. 
Лямбда-функции чаще всего применяют для передачи в качестве аргументов 
в другие функции или для написания более лаконичного кода. 
В этом примере мы собираемся использовать функции sum(), map() и reduce() 
для подсчета элементов в списке, которые делятся на 5.

Приведенный ниже код наглядно демонстрирует это.
"""
from functools import reduce

list_numbers = [78, 99, 66, 44, 50, 30, 45, 15, 25, 20]
result_count = reduce(lambda count, item: count + (item % 5 == 0), list_numbers, 0)

print("количество элементов списка, удовлетворяющих заданному условию:", result_count)
"""
количество элементов списка, удовлетворяющих заданному условию: 6
Надеюсь, что вы узнали о различных подходах к подсчету элементов 
в списке Python с помощью условия или критериев для фильтрации данных.

Удачного обучения!
"""
