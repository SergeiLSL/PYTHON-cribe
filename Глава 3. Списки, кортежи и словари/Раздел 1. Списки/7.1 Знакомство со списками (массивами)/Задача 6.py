"""
Задача №9

На вход программы подаётся набор действительных чисел одной
строкой через пробел. Считайте их в массив и выведите на
печать каждый второй элемент. То есть надо напечатать элементы
с индексами 0, 2, 4, 6 и т.д. Способ вывода - в столбик.

Sample Input:
2.3 5.6 0.12 0.23 12.5 6.7 9.9

Sample Output:
2.3
0.12
12.5
9.9
"""

A = list(map(float, input().split()))

for i in range(0, len(A), 2):
    print(A[i])

# ===============================================
print(*input().split()[::2], sep='\n')

# ===============================================
print('\n'.join(input().split()[::2]))

# ===============================================
print(*list(input().split())[::2],sep='\n')

# ===============================================
print(*[_ for _ in map(float, input().split())][::2], sep = '\n')

# ===============================================
