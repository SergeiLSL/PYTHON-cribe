"""
Задача №8

На вход массива подаётся сначала количество элементов массива n,
а потом сами элементы одной строкой через пробел. Элементы массива - строки.

Затем подаётся число m - количество элементов, которые надо
напечатать одной строкой без пробела.

Считайте данные в массив, и выведите на печать первые m элементов.

Sample Input:
5
Py th on C ++
3

Sample Output:
Python
"""

n = int(input())  # читаем количество элементов в будущем массиве
D = input().split()
m = int(input())

for i in range(m):
    print(D[i], end='')

# ===============================================
input()
print(*input().split()[:int(input())], sep='')

# ===============================================
input()
sp = input().split()
for i in range(int(input())):
    print(sp[i], end='')

# ===============================================
n = int(input())
s = map(str, input().split())
m = int(input())
A = []
for i in range(n):
    for j in s:
        A.append(j)
for i in range(m):
    print (A[i], end = '')

# ===============================================
n = int(input())
print(''.join(input().split()[:int(input())]))

# ===============================================
n = int(input())
lst = input().split()
m = int(input())
print(''.join(lst[:m]))