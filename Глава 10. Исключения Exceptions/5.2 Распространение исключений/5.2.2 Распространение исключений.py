"""
5.2 Распространение исключени

https://boosty.to/egoroff_channel/posts/824db83f-c256-417c-995b-68913d4a30f1
"""


def third():
    print('start third')
    1/0
    print('finish third')


def second():
    print('start second')
    third()
    print('finish second')


def first():
    print('start first')
    try:
        second()
    except ZeroDivisionError:
        print('handling first')  # обработано
    print('finish first')


print('hello1')
first()