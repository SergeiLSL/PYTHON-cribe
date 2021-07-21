"""
5.1 Исключения в Python

https://stepik.org/lesson/427819/step/1?unit=417704
"""
"""
Давайте научимся отлавливать исключения и обрабатывать их
https://habr.com/ru/post/186608/
https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
https://younglinux.info/python/exceptions
"""

print('hello1')
print('hello2')
print('hello3')
# int('hello4')   # вызывает ошибку ValueError: invalid literal for int() with base 10: 'hello4'
print('hello5')
print('hello6')

print('*' * 35)
"""
Чтобы избежать такое исключение добавим специальный блок try-except (попробовать)
"""
a = input()

print('hello1')
print('hello2')
print('hello3')
try:
    int(a)  # вызывает ошибку ValueError: invalid literal for int() with base 10: 'hello4'
except ValueError:
    print('Неправильное преобразование')  # Неправильное преобразование
print('hello5')
print('hello6')

print('+' * 35)

print('hello1')
print('hello2')
print('hello3')
try:
    int(a)  # вызывает ошибку ValueError: invalid literal for int() with base 10: 'hello4'
    print(int(a))
except ValueError:
    print('Неправильное преобразование')  # Неправильное преобразование
print('hello5')
print('hello6')

"""
Все типы исключений являются классами. Все эти классы нахожятся в строгой иеархии.
На самом верху находится Base Exception, ниже 4 исключения (его дочерние классы):
 Exception, SystemExit, GeneralExit, Keyboardinterrupt. 
 И у каждого из них есть свои дочерние классы.
 Для нас важен Exception, вне входят все исключения с которыми мы сталкиваемся при 
 написании кода. Ниже вся структура.
"""

""" Все исключения с переводом на русский язык """
"""
BaseException - базовое исключение, от которого берут начало все остальные.
       SystemExit - исключение, порождаемое функцией sys.exit при выходе из программы.
       KeyboardInterrupt - порождается при прерывании программы пользователем 
       (обычно сочетанием клавиш Ctrl+C).
       GeneratorExit - порождается при вызове метода close объекта generator.
       Exception - а вот тут уже заканчиваются полностью системные исключения 
       (которые лучше не трогать) и начинаются обыкновенные, с которыми можно работать.
            StopIteration - порождается встроенной функцией next, если в итераторе больше нет элементов.
            ArithmeticError - арифметическая ошибка.
                    FloatingPointError - порождается при неудачном выполнении операции с плавающей запятой. 
                    На практике встречается нечасто.
                    OverflowError - возникает, когда результат арифметической операции слишком 
                    велик для представления. Не появляется при обычной работе с целыми 
                    числами (так как python поддерживает длинные числа), но может возникать в 
                    некоторых других случаях.
                    ZeroDivisionError - деление на ноль.
            AssertionError - выражение в функции assert ложно.
            AttributeError - объект не имеет данного атрибута (значения или метода).
            BufferError - операция, связанная с буфером, не может быть выполнена.
            EOFError - функция наткнулась на конец файла и не смогла прочитать то, что хотела.
            ImportError - не удалось импортирование модуля или его атрибута.
            LookupError - некорректный индекс или ключ.
                    IndexError - индекс не входит в диапазон элементов.
                    KeyError - несуществующий ключ (в словаре, множестве или другом объекте).
            MemoryError - недостаточно памяти.
            NameError - не найдено переменной с таким именем.
                    UnboundLocalError - сделана ссылка на локальную переменную в функции, но переменная не определена ранее.
            OSError - ошибка, связанная с системой.
                    BlockingIOError
                    ChildProcessError - неудача при операции с дочерним процессом.
                    ConnectionError - базовый класс для исключений, связанных с подключениями.
                            BrokenPipeError
                            ConnectionAbortedError
                            ConnectionRefusedError
                            ConnectionResetError
                    FileExistsError - попытка создания файла или директории, которая уже существует.
                    FileNotFoundError - файл или директория не существует.
                    InterruptedError - системный вызов прерван входящим сигналом.
                    IsADirectoryError - ожидался файл, но это директория.
                    NotADirectoryError - ожидалась директория, но это файл.
                    PermissionError - не хватает прав доступа.
                    ProcessLookupError - указанного процесса не существует.
                    TimeoutError - закончилось время ожидания.
            ReferenceError - попытка доступа к атрибуту со слабой ссылкой.
            RuntimeError - возникает, когда исключение не попадает ни под одну из других категорий.
            NotImplementedError - возникает, когда абстрактные методы класса требуют 
            переопределения в дочерних классах.
            SyntaxError - синтаксическая ошибка.
                    IndentationError - неправильные отступы.
                            TabError - смешивание в отступах табуляции и пробелов.
            SystemError - внутренняя ошибка.
            TypeError - операция применена к объекту несоответствующего типа.
            ValueError - функция получает аргумент правильного типа, но некорректного значения.
            UnicodeError - ошибка, связанная с кодированием / раскодированием unicode в строках.
                    UnicodeEncodeError - исключение, связанное с кодированием unicode.
                    UnicodeDecodeError - исключение, связанное с декодированием unicode.
                    UnicodeTranslateError - исключение, связанное с переводом unicode.
            Warning - предупреждение.
"""
print('=' * 35)
"""
Каждого класса мы можем создать свой экземпляр.
Например: Создадим экземпляр класса IndexError
"""
t = IndexError()
print(isinstance(t, IndexError))  # True в консоле пишет
print(isinstance(t, LookupError))  # True в консоле пишет
print(isinstance(t, TypeError))  # False в консоле пишет
print(isinstance(t, Exception))  # True  в консоле пишет

print('hello1')
print('hello2')
print('hello3')
try:
    [1, 2][5]  # вызывает ошибку ValueError: invalid literal for int() with base 10: 'hello4'
except ValueError:
    print('Неправильный индекс')  # Неправильный индекс
print('hello5')
print('hello6')