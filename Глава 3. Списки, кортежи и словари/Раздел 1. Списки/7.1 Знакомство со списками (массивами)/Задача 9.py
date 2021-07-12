"""
Задача №12

На вход программы подаётся сначала натуральное чётное
число n - количество элементов массива. Далее подаются
n элементов массива. Элементы массива - строкового типа.
Надо считать массив. Затем выдать элементы массива в таком виде:
на первой строке первый и последний элементы через пробел,
на второй строке второй и предпоследний, на третьей строке -
третий сначала и третий с конца и так далее.

Sample Input:
10
па
ра
ма
ва
ка
фа
ла
да
жа
на

Sample Output:
па на
ра жа
ма да
ва ла
ка фа
"""

n = int(input())     # читаем количество элементов в будущем массиве
A = []               # создали пустой массив (список)
for i in range(n):   # цикл на n повторений
    x = input()
    A.append(x)

for i in range(len(A) // 2):
    print(A[i], A[len(A) - 1 - i], sep=' ')

# ===============================================
a = int(input())
b, c = [[input() for i in range(a//2)] for i in "ab"]
for i in range(a//2):
    print(b[i], c[::-1][i])

# ===============================================
s = [input() for _ in range(int(input()))]
[print(s[i], s[-(i + 1)]) for i in range(len(s) // 2)]

# ===============================================
s = [input() for i in range(int(input()))]
print(*[f'{s[i]} {s[-i - 1]}' for i in range(len(s) // 2)], sep='\n')

# ===============================================
li = [input() for _ in range(int(input()))]

for i in range(int(len(li)/2)):
    print(li[i], li[-i-1])

# ===============================================
count = int(input())
tbl = []
for i in range(count):
    tbl.append(input())
for i in range(len(tbl)//2):
    print(tbl[i], tbl[len(tbl)-1-i])