"""
Модуль random

https://docs.google.com/document/d/13_rGifKmhifA-me4lIkZxSVBmLPlyrKr4PB1kjloOe0/edit#heading=h.42jpvrx7sh91

random позволяет генерировать случайные числа, выбирать случайные элементы
и использовать различные распределения.
Документация к библиотеке: https://docs.python.org/3/library/random.html
Инструкция на русском: https://pythonworld.ru/moduli/modul-random.html

Напишем с помощью random небольшого бота, который смеется над Вашими шутками:
"""
import random
responses = [":D", "Очень смешно!", "Ха-ха-ха", ")))", "Смешная шутка", "Довольно остроумно)"]
joke = input()
while joke != ".":
    print(random.choice(responses))
    joke = input()

"""
Также с помощью random можно проводить эксперименты. 
Например, проверим вероятности выпадения орла и решки после броска монетки:
"""
import random

options = ["heads", "tails"]
heads = tails = 0
n = 10 ** 6
for i in range(n):
    flip = random.choice(options)
    if flip == "heads":
        heads += 1
    else:
        tails += 1
print(heads / n)
print(tails / n)
"""
Без использования программирования провести миллион замеров было бы проблематично.
Задача “Bogosort”
"""