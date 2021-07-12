"""
Как конвертировать строки в datetime

strptime() в Python — это метод из модуля datetime. Вот его синтаксис:

dateobj = datetime.strptime(date_string, format)

Аргументы формата необязательные и являются строками.
Предположим, нужно извлечь текущие дату и время:
"""
import datetime

current_dt = datetime.datetime.now()
print(current_dt)  # 2021-07-03 17:24:45.107068

"""
Результат будет в формате ISO 8601, то есть YYYY-MM-DDTHH:MM:SS.mmmmmm — формат по умолчанию, что позволяет получать строки в едином формате.

Таблица форматов:

Символ	Описание	Пример
%a	День недели, короткий вариант	Wed
%A	Будний день, полный вариант	Wednesday
%w	День недели числом 0-6, 0 — воскресенье	3
%d	День месяца 01-31	31
%b	Название месяца, короткий вариант	Dec
%B	Название месяца, полное название	December
%m	Месяц числом 01-12	12
%y	Год, короткий вариант, без века	18
%Y	Год, полный вариант	2018
%H	Час 00-23	17
%I	Час 00-12	05
%p	AM/PM	PM
%M	Минута 00-59	41
%S	Секунда 00-59	08
%f	Микросекунда 000000-999999	548513
%z	Разница UTC	+0100
%Z	Часовой пояс	CST
%j	День в году 001-366	365
%U	Неделя числом в году, Воскресенье первый день недели, 00-53	52
%W	Неделя числом в году, Понедельник первый день недели, 00-53	52
%c	Локальная версия даты и времени	Mon Dec 31 17:41:00 2018
%x	Локальная версия даты	12/31/18
%X	Локальная версия времени	17:41:00
%%	Символ “%”	%
"""
import datetime

date_string = "11/17/20"
date_obj = datetime.datetime.strptime(date_string, '%m/%d/%y')
print(date_obj)  # 2020-11-17 00:00:00
date_obj2 = datetime.datetime.strptime(date_string, '%m/%d/%y')
print(date_obj2)  # 2020-11-17 00:00:00

"""
Примеры конвертации строки в объект datetime с помощью strptime

Предположим, что есть следующая строка с датой: «11/17/20 15:02:34», 
и ее нужно конвертировать в объект datetime.
"""
from datetime import datetime

datetime_string = "11/17/20 15:02:34"
datetime_obj = datetime.strptime(datetime_string, '%m/%d/%y %H:%M:%S')
print(datetime_obj)  # 2020-11-17 15:02:34

"""
Даты могут быть записаны в разных форматах. 
Например, следующие даты отличаются лишь представлением:

Friday, November 17, 2020;
11/17/20;
11–17–2020.
Вот как это работает:
"""
from datetime import datetime

# создадим даты как строки
ds1 = 'Friday, November 17, 2020'
ds2 = '11/17/20'
ds3 = '11-17-2020'
ds4 = '07/03/21'
ds5 = '07.03.2021'
ds6 = '22.08.2019'

# Конвертируем строки в объекты datetime и сохраним
dt1 = datetime.strptime(ds1, '%A, %B %d, %Y')
dt2 = datetime.strptime(ds2, '%m/%d/%y')
dt3 = datetime.strptime(ds3, '%m-%d-%Y')
dt4 = datetime.strptime(ds4, '%m/%d/%y')
dt5 = datetime.strptime(ds5, '%m.%d.%Y')
dt6 = datetime.strptime(ds6, '%d.%m.%Y')

print(dt1)  # 2020-11-17 00:00:00
print(dt2)  # 2020-11-17 00:00:00
print(dt3)  # 2020-11-17 00:00:00
print(dt4)  # 2021-07-03 00:00:00
print(dt5)  # 2021-07-03 00:00:00
print(dt6)  # 2019-08-22 00:00:00

"""
Как конвертировать объект datetime в строку

Модуль datetime в Python содержит метод strftime(), который делает обратное 
(то есть, конвертирует объект datetime и time в строки). Вот его синтаксис:

datetime_string = datetime_object.strftime(format_string)
time_string = datetime_object.strftime(format_string[,time_object]
"""
"""
Примеры конвертации datetime в строку с помощью strftime()
Предположим, нужно конвертировать текущий объект datetime в строку. 
Сначала нужно получить представление объекта datetime и 
вызвать на нем метод strftime().
"""
import datetime

current_date = datetime.datetime.now()
current_date_string = current_date.strftime('%m/%d/%y %H:%M:%S')
print(current_date_string)  # 07/03/21 17:42:00
current_date_string2 = current_date.strftime('%m/%d/%y')
current_date_string3 = current_date.strftime('%d/%m/%y')
current_date_string4 = current_date.strftime('%d.%m.%y')

print(current_date_string)  # 07/03/21 17:42:00
print(current_date_string2)  # 07/03/21
print(current_date_string3)  # 03/07/21
print(current_date_string4)  # 03.07.21
print('*' * 25)
# Так и не пойму как вернуть в строку
# current_date1 = datetime.datetime(2020-11-17)
# current_date_string5 = current_date1.strftime('%d/%m/%y')
# print(current_date_string5)  # 03.07.21
"""
Как получить строковое представление даты и времени с помощью функции format()

Пример №1. Конвертация текущей временной метки в объекте datetime в строку 
в формате «DD-MMM-YYYY (HH:MM:SS:MICROS)»:
"""
import datetime

dt_obj = datetime.datetime.now()
dt_string = dt_obj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
print('Текущее время : ', dt_string)  # Текущее время :  03-Jul-2021 (17:44:16.469191)

"""
Пример №2. Конвертация текущей временной метки объекта datetime в строку 
в формате «HH:MM:SS.MICROS – MMM DD YYYY».
"""
import datetime

dt_obj = datetime.datetime.now()
dt_string = dt_obj.strftime("%H:%M:%S.%f - %b %d %Y")
print('Текущее время : ', dt_string)  # Текущее время :  17:45:21.314821 - Jul 03 2021
