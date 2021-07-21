"""
5.1 Исключения в Python

https://stepik.org/lesson/427819/step/1?unit=417704
"""
"""
Все исключения вместе:
"""


def printExcTree(thisclass, nest = 0):

    if nest > 1:

        print(" |" * (nest - 1), end="")

    if nest > 0:

        print(" +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():

        printExcTree(subclass, nest + 1)


#printExcTree(BaseException)
"""
BaseException
 +---Exception
 | +---TypeError
 | +---StopAsyncIteration
 | +---StopIteration
 | +---ImportError
 | | +---ModuleNotFoundError
 | | +---ZipImportError
 | +---OSError
 | | +---ConnectionError
 | | | +---BrokenPipeError
 | | | +---ConnectionAbortedError
 | | | +---ConnectionRefusedError
 | | | +---ConnectionResetError
 | | +---BlockingIOError
 | | +---ChildProcessError
 | | +---FileExistsError
 | | +---FileNotFoundError
 | | +---IsADirectoryError
 | | +---NotADirectoryError
 | | +---InterruptedError
 | | +---PermissionError
 | | +---ProcessLookupError
 | | +---TimeoutError
 | | +---UnsupportedOperation
 | +---EOFError
 | +---RuntimeError
 | | +---RecursionError
 | | +---NotImplementedError
 | | +---_DeadlockError
 | +---NameError
 | | +---UnboundLocalError
 | +---AttributeError
 | +---SyntaxError
 | | +---IndentationError
 | | | +---TabError
 | +---LookupError
 | | +---IndexError
 | | +---KeyError
 | | +---CodecRegistryError
 | +---ValueError
 | | +---UnicodeError
 | | | +---UnicodeEncodeError
 | | | +---UnicodeDecodeError
 | | | +---UnicodeTranslateError
 | | +---UnsupportedOperation
 | +---AssertionError
 | +---ArithmeticError
 | | +---FloatingPointError
 | | +---OverflowError
 | | +---ZeroDivisionError
 | +---SystemError
 | | +---CodecRegistryError
 | +---ReferenceError
 | +---MemoryError
 | +---BufferError
 | +---Warning
 | | +---UserWarning
 | | +---DeprecationWarning
 | | +---PendingDeprecationWarning
 | | +---SyntaxWarning
 | | +---RuntimeWarning
 | | +---FutureWarning
 | | +---ImportWarning
 | | +---UnicodeWarning
 | | +---BytesWarning
 | | +---ResourceWarning
 | +---Error
 | +---_OptionError
 | +---error
 | +---Verbose
 +---GeneratorExit
 +---SystemExit
 +---KeyboardInterrupt
"""


print('hello1')
print('hello2')
print('hello3')
# 'hello4'[9]  - вызывает ошибку IndexError: string index out of range
print('hello4')
print('hello5')
print('hello6')

print('hello1')
print('hello2')
print('hello3')
# print(a + b)  # - вызывает ошибку NameError: name 'a' is not defined
print('hello4')
print('hello5')
print('hello6')

"""
Исключения бывают:
1. Выполнения - они обнаруживаются в момент выполнения программы. 
Программа останавливается в процессе выполнени
2. До выполнения (исключения компеляции) IndentationError: unexpected indent -  например
неправильный отступ. Программа даже не запускается.
"""
"""
Так же не стоит путать исключения и ошибка. Ошибку тоже можно назвать исключением, 
но ошибки еще бывают и логического типа. 
"""


