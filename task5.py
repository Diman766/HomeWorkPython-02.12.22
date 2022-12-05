# Даны два файла,в каждом из которых находится запись многочлена.
# Задача - сформировать файл,содержащий сумму многочленов.

from itertools import zip_longest

file1 = open('file1task5.txt', 'r')
string1 = file1.read()
file1.close

file2 = open('file2task5.txt', 'r')
string2 = file2.read()
file2.close

def sortString (string):
    string = string.split('+')
    
    for i in range(len(string)):
        string[i] = string[i].split('*')
        string[i] = string[i][:1]

    string = [x for l in string for x in l]
    string = list(map(int, string))
    # string = [int(string[i]) for i in range(len(string))]
    string.reverse()
    return string

result = [sum(x) for x in zip_longest(sortString(string1), sortString(string2), fillvalue=0)] 
result.reverse()

k = len(result)-1
number = str(result[0])
string = number + '*x**' + str(k)
stringResult = string
k -= 1

while k >= 0:
    if k == 1:
        randomNumber = str(result[-k-1])
        string = '+' + randomNumber + '*x'
        stringResult += string
        k -= 1
    elif k == 0:
        randomNumber = str(result[-k-1])
        string = '+' + randomNumber 
        stringResult += string
        k -= 1
    elif k > 1:
        randomNumber = str(result[-k-1])
        string = '+' + randomNumber + '*x**' + str(k)
        stringResult += string
        k -= 1
print(stringResult)

file = open('fileResTask5.txt', 'a')
file.writelines(stringResult + '\n')
file.close