s = "м_ма"
print(s.isalpha())


# list.append(x) Добавляет элемент в конец списка
list_a = [1, 2, 3, 'asd']
print(list_a)  # [1, 2, 3, 'asd']
# list.append(35)
print(list_a)  # [1, 2, 3, 'asd', 35]

"""
l

list.append(x) Добавляет элемент в конец списка

list.extend(L) Расширяет список list, добавляя в конец все элементы списка L

list.insert(i, x) Вставляет на i-ую позицию элемент x

list.remove(x) Удаляет первый элемент в списке, имеющий значение x.
ValueError, если такого элемента не существует

list.pop([i]) Удаляет i-ый элемент и возвращает его.
Если индекс не указан, удаляется последний элемент

list.index(x, [start [, end]]) Возвращает индекс первого
элемента со значением x (при этом поиск ведется от start до end)

list.count(x) Возвращает количество элементов со значением x

list.sort() Сортирует список

list.reverse() Разворачивает список

list.copy() Поверхностная копия списка

list.clear() Очищает список
"""