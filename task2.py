# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число  '))

def multipliers(n):
    i = 2
    multiplier = []
    while i * i <= n:
        while n % i == 0:
            n /= i
        multiplier.append(i)
        i += 1
    if n > 1:
        multiplier.append(int(n))
    return multiplier

print(multipliers(n))
