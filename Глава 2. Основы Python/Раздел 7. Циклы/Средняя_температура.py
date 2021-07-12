# Подсчет средней температуры за несколько дней

total = 0
days = 0
temperature = float(input())
while temperature != 0:
    total += temperature
    days += 1
    temperature = float(input())
    print(total/days)