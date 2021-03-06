"""
Задача №11

На вход программы подаётся сначала натуральное число -
количество элементов в массиве. Затем сами элементы.
Элементы массива - целые числа. Элементы подаются по одному в строке.

Напишите программу, которая считает массив целых чисел,
а затем напечатает его в зеркальном отображении.
Первый элемент на последнем месте, второй на предпоследнем и так далее.

Для вывода используйте цикл for с шагом -1.

Sample Input:
5
1
2
3
4
5

Sample Output:
5 4 3 2 1
"""

n = int(input())     # читаем количество элементов в будущем массиве
A = []               # создали пустой массив (список)
for i in range(n):   # цикл на n повторений
    x = int(input())
    A.append(x)

for i in range(len(A) - 1, -1, -1):
    print(A[i], end=' ')

# ===============================================
[print(i, end=' ') for i in [int(input()) for _ in range(int(input()))][::-1]]

# ===============================================
n = int(input())
new = []
for i in range(n):
    num = input()
    new.append(num)
print(' '.join(new[::-1]))

# ===============================================
print(*[input() for i in '!' * int(input())][::-1])

# ===============================================
print(' '.join([input() for i in '!' * int(input())][::-1]))

# ===============================================
print(*reversed([int(input()) for _ in range(int(input()))]))