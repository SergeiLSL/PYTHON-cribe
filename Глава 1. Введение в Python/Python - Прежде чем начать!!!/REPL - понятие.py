""" REPL """

"""
    REPL (от англ. read-eval-print loop — «цикл „чтение — вычисление — вывод“») 
 — форма организации простой интерактивной среды программирования в рамках 
 средств интерфейса командной строки. Чаще всего этой аббревиатурой характеризуется 
 интерактивная среда языка программирования Лисп, однако такая форма характерна 
 и для интерактивных сред языков Java, Smalltalk, Perl, Python, Swift, Ruby, 
 Haskell, Scala, Groovy, JavaScript, Erlang, PHP и других.

    В такой среде пользователь может вводить выражения, которые среда тут же будет 
 вычислять, а результат вычисления отображать пользователю. Названия элементов цикла 
 связаны с соответствующими примитивами Лиспа:
    - функция read читает одно выражение и преобразует его в соответствующую структуру 
    данных в памяти;
    - функция eval принимает одну такую структуру данных и вычисляет соответствующее 
    ей выражение;
    - функция print принимает результат вычисления выражения и печатает его пользователю.
    
    Чтобы реализовать REPL-среду для некоторого языка, достаточно реализовать три функции: 
 чтения, вычисления и вывода, и объединить их в бесконечный цикл. REPL-среда очень удобна 
 при изучении нового языка, так как предоставляет пользователю быструю обратную связь.
"""