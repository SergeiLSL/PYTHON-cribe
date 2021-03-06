""" МЕТОДЫ СТРОК """

"""
S1 + S2 Конкатенация (сложение строк)

S1 * 3 Повторение строки

S[i] Обращение по индексу

S[i:j:step] Извлечение среза

len(S) Длина строки

S.find(str, [start],[end]) Поиск подстроки в строке.
Возвращает номер первого вхождения или -1

S.rfind(str, [start],[end]) Поиск подстроки в строке.
Возвращает номер последнего вхождения или -1

S.replace(шаблон, замена) Замена шаблона

S.split(символы) Разбиение строки по разделителю

S.isdigit() Состоит ли строка из цифр

S.isalpha() Состоит ли строка из букв

S.isalnum() Состоит ли строка из цифр или букв

S.upper() Преобразование строки к верхнему регистру

S.lower() Преобразование строки к нижнему регистру

S.startswith(str) Начинается ли строка S с шаблона str

S.endswith(str) Заканчивается ли строка S шаблоном str

ord(символ) Символ в его код ASCII

chr(число) Код ASCII в символ

S.capitalize() Переводит первый символ строки в верхний регистр,
а все остальные в нижний

S.swapcase() Переводит символы нижнего регистра в верхний,
а верхнего – в нижний

S.lstrip() Удаление пробельных символов в начале строки

S.rstrip() Удаление пробельных символов в конце строки

S.strip() Удаление пробельных символов в начале и в конце строки
"""