"""
5.2 Распространение исключени

https://boosty.to/egoroff_channel/posts/824db83f-c256-417c-995b-68913d4a30f1
"""

print('hello1')
print('hello2')
print('hello3')
# 1/0  # ZeroDivisionError: division by zero
print('hello4')
print('hello5')
print('hello6')

print('*' * 25)
"""
Посмотрим как будут вести себя исключения, если они произойдут в функции.
"""


def first():
    print('start first')
    # 1 / 0  # ZeroDivisionError: division by zero
    print('finish first')


print('hello1')
first()

print('+' * 25)


def second():
    print('start second')
    # 1 / 0  # ZeroDivisionError: division by zero
    print('finish second')


def first():
    print('start first')
    second()
    print('finish first')


print('hello1')
first()

print('+' * 25)


def third():
    print('start third')
    try:
        1 / 0  # ZeroDivisionError: division by zero
    except ZeroDivisionError:
        print('handling')  # обработано
    print('finish third')


def second():
    print('start second')
    third()
    print('finish second')


def first():
    print('start first')
    second()
    print('finish first')


print('hello1')
first()