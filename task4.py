#  Задана натуральная степень k.
#  Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0 5

import random

k = int(input('Введите степень  '))

randomNumber = str(random.randint(0, 100))
string = randomNumber + '*x**' + str(k)
stringResult = string
k -= 1

while k >= 0:
    if k == 1:
        randomNumber = str(random.randint(0, 100))
        string = '+' + randomNumber + '*x'
        stringResult += string
        k -= 1
    elif k == 0:
        randomNumber = str(random.randint(0, 100))
        string = '+' + randomNumber + '=0'
        stringResult += string
        k -= 1
    elif k > 1:
        randomNumber = str(random.randint(0, 100))
        string = '+' + randomNumber + '*x**' + str(k)
        stringResult += string
        k -= 1
print(stringResult)

file = open('filetask4.txt', 'a')
file.writelines(stringResult + '\n')
file.close
