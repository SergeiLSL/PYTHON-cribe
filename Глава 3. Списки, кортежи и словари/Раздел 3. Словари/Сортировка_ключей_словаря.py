# Для того, чтобы вывести содержимое словаря в отсортированном
# по возрастанию ключей виде, используется функция sorted().
# Она сортирует ключи словаря и помещает их в список.

def fill_list(m1, m2, amount, l):
    from random import randint
    for i in range(amount):
        l.append(randint(m1, m2))


def analysis(your_list, your_dict):
    for i in your_list:
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1


lst = []
dct = {}

mn = int(input('Минимум: '))
mx = int(input('Максимум: '))
qty = int(input('Количество элементов: '))

fill_list(mn, mx, qty, lst)
analysis(lst, dct)

for item in sorted(dct):
    print("'%d':%d" % (item, dct[item]))