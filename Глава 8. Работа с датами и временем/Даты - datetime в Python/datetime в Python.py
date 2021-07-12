# https://pythonru.com/primery/kak-ispolzovat-modul-datetime-v-python
# https://metanit.com/python/tutorial/8.2.php

"""
Например, узнаем какой временной период между двумя датами:
"""
from datetime import timedelta, datetime

now = datetime.now()
print(now, type(now))
twenty_two_may = datetime(2021, 5, 22)
period = twenty_two_may - now

print("{} дней  {} секунд   {} микросекунд".format(period.days, period.seconds, period.microseconds))
print("{} дней".format(period.days))
print("Всего: {} секунд".format(period.total_seconds()))


"""
Сравнение дат
Также как и строки и числа, даты можно сравнивать с помощью 
стандартных операторов сравнения:
"""
print('*' * 30)

from datetime import datetime

now = datetime.now()
deadline = datetime(2021, 4, 22)
print(deadline)
if now > deadline:
    print("Срок сдачи проекта прошел")
elif now.day == deadline.day and now.month == deadline.month and now.year == deadline.year:
    print("Срок сдачи проекта сегодня")
else:
    period = deadline - now
    print("Осталось {} дней".format(period.days))
