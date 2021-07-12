""" Комментирование Python кода """

"""
Программирование отражает ваш образ мышления, чтобы описать отдельные шаги, 
которые вы предприняли для решения проблемы с помощью компьютера. 
Комментирование вашего кода помогает объяснить ваш мыслительный процесс, 
а также помогает вам и другим людям понять смысл вашего кода. 
Это позволяет вам легче находить ошибки, исправлять их, впоследствии улучшать 
код, а также повторно использовать его и в других приложениях.

Комментирование важно для всех видов проектов, независимо от того, 
маленькие они, средние или довольно большие. Это важная часть вашего 
рабочего процесса, и считается хорошей практикой для разработчиков. 
Без комментариев все может запутаться, очень быстро. В этой статье 
мы расскажем о различных методах комментирования, поддерживаемых Python,
и о том, как его можно использовать для автоматического создания 
документации для вашего кода с использованием так называемых строк 
документации уровня модуля.

Хорошие против плохих комментариев
Как бы ни были важны комментарии, все еще можно писать плохие комментарии. 
Они всегда должны быть короткими, прямолинейными и добавлять информативную 
ценность.

Например, это довольно бесполезный комментарий:
"""
b = 56  # assigning b a value of 56 (присваиваем b значение 56)

"""
Следующий пример демонстрирует более полезный комментарий и дает 
переменным очевидные имена:
"""
salestax10 = 1.10  # defining a sales tax of 10% (определение налога с продаж в размере 10%)
salestax20 = 1.20  # defining a sales tax of 20% (определение налога с продаж в размере 20%)

"""
Существует бесконечное количество других сценариев, которые заслуживают 
комментариев. Это только один пример. Хорошее практическое правило - 
добавлять комментарии к любой строке кода (например, к списку) или 
к фрагменту кода, цель которого не очевидна. Это очень субъективно, 
и на самом деле это навык, который необходимо изучить.
"""
"""
Типы комментариев
Комментарий в Python начинается с символа хеша # и продолжается до 
конца физической строки. Однако хеш-символ внутри строкового значения 
не рассматривается как комментарий. Если быть точным, комментарий 
можно написать тремя способами - полностью в отдельной строке, рядом 
с оператором кода и в виде многострочного блока комментариев.

В следующих разделах я опишу каждый тип комментария.

Однострочные комментарии
Такой комментарий начинается с хеш-символа ( #) и сопровождается текстом, 
который содержит дополнительные пояснения.
"""
# defining the post code (определение почтового индекса)
postCode = 75000
"""
Вы также можете написать комментарий рядом с оператором кода. 
Следующий пример показывает, это:
"""
# define the general structure of the product with default values
# определить общую структуру продукта со значениями по умолчанию

product = {
    "productId": 0,  # product reference id, default: 0 (Идентификатор ссылки на продукт, по умолчанию)
    "description": "",  # item description, default: empty (описание товара, по умолчанию: пусто)
    "categoryId": 0,  # item category, default: 0 (категория элемента, по умолчанию: 0)
    "price": 0.00  # price, default: 0.00 (цена, по умолчанию: 0.00)
}
"""
Руководство по стилю для кода Python ( PEP8 ) рекомендует менее 79 
символов на строку. На практике 70 или 72 символа в строке легче 
читать, и поэтому рекомендуется. Если ваш комментарий приближается 
к этой длине или превышает ее, тогда вы захотите распределить его 
по нескольким строкам.
"""

"""
Многострочные комментарии
Как уже упоминалось выше, весь блок комментариев также понимается Python. 
Эти комментарии служат встроенной документацией для других, читающих 
ваш код, и обычно объясняют вещи более подробно.

Технически Python не имеет явной поддержки многострочных комментариев, 
поэтому некоторые варианты считаются обходным решением, но все же работают 
для многострочных комментариев.

Версия 1 объединяет однострочные комментарии следующим образом:
"""
# LinuxThingy version 1.6.5               (LinuxThingy версии 1.6.5)
#
# Parameters:                              Параметры:
#
# -t (--text): show the text interface     -t (--text): показать текстовый интерфейс
# -h (--help): display this help           -h (--help): показать эту справку

"""
Версия 2 проще, чем версия 1. Изначально она предназначалась для 
создания документации (подробнее об этом ниже), но ее также можно 
использовать для многострочных комментариев.
"""
"""
LinuxThingy version 1.6.5

Parameters:

-t (--text): show the text interface
-h (--help): display this help
"""
# Обратите внимание, что последняя версия должна быть заключена
# в специальные кавычки ( """) для работы, а не хеш-символы.


"""
Обычная практика

Довольно часто начинать Python-файл с нескольких строк комментариев. 
В этих строках указывается информация о проекте, назначении файла, 
программисте, который его разработал или работал над ним, и лицензии 
на программное обеспечение, которое используется для кода.

Этот фрагмент взят из одного из примеров, которые я использую в 
учебных целях. Комментарий начинается с описания, за ним следует 
уведомление об авторских правах с моим именем и год публикации кода. 
Ниже вы увидите, что код лицензирован под GNU Public License ( GPL ). 
Для того, чтобы связаться со мной, мой адрес электронной почты также 
добавлен туда.
"""
# -----------------------------------------------------------
# demonstrates how to write ms excel files using python-openpyxl
#
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------


"""
Комментарии документации
Python имеет встроенную концепцию под названием «строки документации», 
которая является отличным способом связать написанную вами документацию 
с модулями, функциями, классами и методами Python. Строка документа 
добавляется в качестве комментария прямо под заголовком функции, модуля 
или объекта и описывает действия функции, модуля или объекта. 
Ожидается, что будут следовать этим правилам:

Строка документа - это либо однострочный, либо многострочный комментарий. 
В последнем случае первая строка является кратким описанием, а после 
первой строки следует пустая строка.

Начните строку документа с заглавной буквы и завершите ее точкой.

Это основной пример того, как это выглядит:
"""


def add(value1, value2):
    """Calculate the sum of value1 and value2."""
    return value1 + value2


print(add(2, 5))  # 7
print(add.__doc__)  # Calculate the sum of value1 and value2.


def mull(value1, value2):
    """Calculate the mull value1 and value2."""
    return value1 * value2


print(mull(2, 5))  # 10
print(mull.__doc__)  # Calculate the mull value1 and value2.


def volume(value1, value2, value3):
    """Вычисляет объем куба со сторонами value1, value2, value3"""
    return value1 * value2 * value3


print(volume(2, 5, 10))  # 100
print(volume.__doc__)  # Вычисляет объем куба со сторонами value1, value2, value3
"""
В интерактивной справочной системе Python строка документации 
становится доступной через атрибут __doc__.
"""
print(add.__doc__)  # Calculate the sum of value1 and value2.
"""
Существует ряд инструментов, которые автоматически генерируют 
документацию из строк документации, таких как Doxygen, PyDoc, 
pdoc и расширение autodoc для Sphinx. Мы объясним вам, как работать 
с ними в следующей статье.
"""

"""
Заключение
Написание правильных комментариев в вашем коде Python не так сложно, 
и вам просто нужна сила выносливости. Это помогает всем, кто пытается 
понять ваш код, включая вас самих, когда вы в следующий раз вернетесь 
к нему. Мы надеемся, что совет, который мы дали вам здесь, облегчит 
вам создание более качественных комментариев и документации в вашем коде.
"""

print(volume(20, 50, 100))  #
print(volume.__doc__)  # Вычисляет объем куба со сторонами value1, value2, value3

