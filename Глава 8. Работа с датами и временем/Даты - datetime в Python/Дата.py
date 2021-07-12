"""
datetime включает различные компоненты. Так, он состоит из объектов следующих типов:

date — хранит дату
time — хранит время
datetime — хранит дату и время
"""
"""
Как получить текущие дату и время?

С помощью модуля Python это сделать очень просто. 
Сначала нужно импортировать класс datetime из модуля datetime, 
после чего создать объект datetime. 
Модуль предоставляет метод now(), который возвращает 
текущие дату и время с учетом локальных настроек.
"""
import datetime

dt_now = datetime.datetime.now()
print(dt_now)  # 2021-07-03 16:32:41.009381

"""
Получить текущую дату в Python

Класс date можно использовать для получения или изменения объектов даты. 
Например, для получения текущей с учетом настроек подойдет следующее:
"""
from datetime import date

current_date = date.today()
print(current_date)  # 2021-07-03
# Текущая дата — 2020-11-14 в формате год-месяц-день соответственно.

"""
Получить текущее время

Для получения текущего локального времени сперва нужно получить
текущие дату и время, а затем достать из этого объекта только
время с помощью метода time():
"""
import datetime

current_date_time = datetime.datetime.now()
current_time = current_date_time.time()
print(current_time)  # 16:25:24.779155

"""
Компоненты datetime в Python

Модуль datetime в Python может использоваться для получения разных 
версий времени. Для этого нужно ознакомиться с атрибутами модуля. 
Используем для этого функцию dir().
"""
import datetime

attr = dir(datetime)
print(attr)  # ['MAXYEAR', 'MINYEAR', '__doc__', '__name__', '__package__',
# 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'tzinfo']
"""
В этом руководстве речь пойдет о следующих элементах:

date — объекты даты
datetime — объекты даты и времени
time — объекты времени
timedelta — этот атрибут покрывает интервалы и используется для 
определения прошлых или будущих событий
Tzinfo — этот атрибут отвечает за часовые пояса
"""

"""
Как создавать объекты даты и времени

Для создания объекта времени используется класс time из модуля 
datetime в Python. Синтаксис следующий: datetime.time(hour, minutes, seconds).

В этом примере создается объект времени представленный следующим образом (8, 48, 45).
"""
import datetime

timeobj = datetime.time(8, 48, 45)
print(timeobj)  # 08:48:45
"""
Сначала импортируется модуль datetime. После этого создается экземпляр 
класса (объект time). Затем ему присваивается значение datetime.time(8, 48, 45), 
где параметры 8, 48 и 45 представляют собой часы, минуты и секунды соответственно.

Для создания объекта даты нужно передать дату с использованием следующего синтаксиса:
"""
# datetime.datetime(year, month, day))
# Такой пример:
import datetime

date_obj = datetime.datetime(2020, 10, 17)
print(date_obj)  # 2020-10-17 00:00:00

"""
Timedelta

timedelta представляет длительность (даты или времени). 
Модуль datetime включает атрибут timedelta(), который используется 
для управления датой в Python. Объект timedelta выглядит следующим образом:

td_object =timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
td_object
datetime.timedelta(0)
Все аргументы опциональные и их значения по умолчанию равно 0. 
Они могут быть целыми или числами с плавающей точкой, как положительными, 
так и отрицательными. Благодаря этому можно выполнять математические операции, 
такие как сложение, вычитание и умножение.
"""

"""
Как вычислить разницу для двух дат

Посмотрим на несколько примеров вычисления разницы во времени. 
Предположим, есть два объекта datetime:
"""
# first_date = date(2020, 10, 2)
# second_date = date(2020, 10, 30)
# Для получения разницы нужно лишь вычесть значение одного объекта из второго:
from datetime import date

first_date = date(2020, 10, 2)
second_date = date(2020, 10, 30)
delta = second_date - first_date
print(delta)  # 28 days,0:00:00
# Таким образом между 2 и 30 октября 2020 года 28 дней.

"""
Как вычислить разницу двух объектов datetime.time

С помощью timedelta нельзя выполнять манипуляции над объектами time. 
Например:
"""

# from datetime import datetime, timedelta
#
# current_datetime = datetime.now()
# current_time = current_datetime.time()
# print("Текущее время:", current_time)
# tm_after_1_hr = current_time + timedelta(hours=1)
# print(tm_after_1_hr)
#
# Такой код вернет следующую ошибку:
#
# Traceback (most recent call last):
#   File "C:\Users\alex\AppData\Local\Programs\Python\Python38\sg_verify.py", line 6, in <module>
#     tm_after_1_hr = current_time + timedelta(hours=1)
# TypeError: unsupported operand type(s) for +: 'datetime.time' and 'datetime.timedelta'

"""
Как получать прошлые и будущие даты с помощью timedelta

Поскольку timedelta — это длительность, то для получения прошлой 
или будущей даты нужно добавить объект timedelta к существующему 
или вычесть из него же. Вот пример нескольких уравнений, 
где n — это целое число, представляющее количество дней:
"""

# import datetime
#
# current_date = datetime.datetime.today()
# past_date = datetime.datetime.today() – datetime.timedelta(days=n)
# future_date = datetime.datetime.today() – datetime.timedelta(days=n)
"""
Если нужно, например, получить дату за прошлые две недели, 
то достаточно вычесть 14 дней из текущей даты:
"""
import datetime

past_date = datetime.datetime.today() - datetime.timedelta(days=14)
print(past_date)  # 2020-10-31 16:12:09.142258

"""
Предположим, вы задумали практиковать определенный навык в течение 21 дня. 
Для получения будущей даты нужно добавить 21 день к текущей дате:
"""
import datetime

future_date = datetime.datetime.today() + datetime.timedelta(days=21)
print(future_date)  # 2021-07-24 17:21:30.323778
