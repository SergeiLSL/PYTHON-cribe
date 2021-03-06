"""
Списки, массивы

http://itrobo.ru/programmirovanie/python/massivy-v-python.html

До сих пор мы использовали отдельно взятые переменные строкового
или числового типа и нам их пока хватало для решения задач.
Но если взглянуть шире на то, с какими данными приходится иметь
дело в жизни, то можно заметить, что люди часто имеют дело с
большими наборами данных.

Например, мы хотим записывать день за днём температуру
воздуха в июне месяце в течение 30 дней, для того, чтобы
получить потом статистическую информацию: максимальную и
минимальную температуру в июне, а также среднюю температуру
этого месяца. При этом получится достаточно большой  набор
данных. И хранить их в 30 различных переменных очень накладно!
Только представьте:

t1 = 20
t2 = 21
t3 = 19
......
t30 = 28

При обработке этих переменных будет получаться огромный, неудобный код!

Выход для таких ситуаций конечно придуман. Такие данные хранят
в виде массивов. Простое определение массива звучит так:
Массив - это упорядоченный набор однотипных данных. Массиву
присваивается имя, с помощью которого можно ссылаться как на
массив данных в целом, так и на любой его элемент.
Обращаем внимание на 2 момента:

1) Упорядоченный набор
2) Данные однотипные

# Пример хранения дневных температур за июнь месяц за 10 дней

Temp = [20, 21, 19, 22, 23, 19, 24, 25, 24, 25]
# Индексы 0  1   2   3   4   5   6   7   8   9

# В языке Python также используется отрицательная индексация, как в строках

       -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
Temp = [20, 21, 19, 22, 23, 19, 24, 25, 24, 25]


Фраза упорядоченный набор означает, что каждый элемент стоит
на своём месте и он будет иметь индекс, точно также, как имел
индекс каждый элемент строкового типа.

Разберёмся, что значит однотипные данные. Обычно в условиях
задач и соответственно в жизни, приходится иметь дело с набором
данных одного типа, например, с целочисленными данными или
со строковыми данными.

Однако в языке Python можно создать набор, который позволит
хранить разные типы данных и такой набор называется списком -
служебное слово list. Но в учебных задачах мы будем иметь
именно с однотипными данными. То есть структуру list мы будем
использовать в режиме массива.

# В Python нет массива в чистом виде. В этом языке можно использовать
разные типы данных в наборе.
# Такая структура данных называется - list:
"""
A = [1, 2, 3, "a", "b", "c", 1.1, 1.2, 1.3 ]
"""
# Но в учебных задачах вы будете обрабатывать однотипные данные, 
поэтому в условии задачи будет звучать слово массив:
"""
A = [1, 2, 3, 4, 5, 6]        # целочисленный массив
B = ["ba", "ca", "da", "ka"]  # массив строк
С = [2.4, 3.5, 7.8, 8.9]      # массив действительных чисел
"""
Создание массива (списка)

Научимся создавать массив в тексте программы,  
выводить его целиком и отдельные элементы. 

1) Массив можно создать в тексте программы. Для этого сами 
придумываем ему имя и записываем внутри квадратных скобок 
через запятую элементы массива: 
"""
A = [1, 2, 3, 4, 5, 6]        # целочисленный массив
B = ["ba", "ca", "da", "ka"]  # массив строк
С = [2.4, 3.5, 7.8, 8.9]      # массив действительных чисел
"""
2) Можно создать массив, состоящий из одинаковых элементов. 
Часто в начале программы нужен массив, состоящий только из одних нулей:
"""
F = [0] * 10  # создание массива, котроый содержит 10 нулей
"""
3) Можно создать пустой массив, подобно тому, как мы создавали пустую строку:
"""
H = []  # этот массив пока пустой, но в него можно добавлять элементы
"""
4) Создать новый массив можно "склеиванием" имеющихся. 
Опять же полная аналогия работы со строками:
"""
A = [1, 2, 3, 4, 5]
B = [6, 7, 8, 9, 10]
C = A + B
print(C)
"""
Вывод элементов массива и самого массива:

1) Для того, чтобы обратиться к элементу массива, надо указать 
имя массива и в квадратных скобках индекс элемента:
"""
B = ["ba", "ca", "da", "ka"]
print(B[0])   # помним, что индексация начинается с 0
print(B[-1])  # в Python есть отрицательные индексы, легко обратиться к последнему элементу
"""
2) Для того, чтобы напечатать массив, можно написать просто print(B):
"""
B = ["ba", "ca", "da", "ka"]
print(B)  # такой вывод печатает скобки и запятые: ["ba", "ca", "da", "ka"]
"""
Такой вывод массива будете использовать для себя, во время 
тестирования и отладки программы. Так как в тестирующую систему надо 
отправлять результат работы без лишних знаков.

3) Можно вывести массив без скобок, используя звёздочку перед 
названием массива. Но этот способ самый медленный. Использовать 
только в тех случаях, когда массивы небольшого размера и в  
процессе тестирования и отладки программы:
"""
B = ["ba", "ca", "da", "ka"]
print(*B)  # ba ca da ka это самый МЕДЛЕННЫЙ вывод массива
