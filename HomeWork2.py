# ДЗ семинар 2
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые –
# гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть

# n = int(input('Введите количество монеток на столе: '))
# orel = 0
# reshka = 0
# for i in range(n):
#    x = int(input())
#    if x == 1:
#        reshka+=1
#    else:
#        orel+=1
# print(min(orel, reshka))          

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S 
# и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# s = int(input('Сумма загаданных чисел: '))
# p = int(input('Произведение загаданных чисел: '))
# for x in range(s):
#    for y in range(p):
#       if x + y == s and x * y == p:
#           print(f'Загаданные числа: {x} , {y}')
#            break

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# n = int(input('Ограничение степеней 2: '))
# degree = 0
# while 2 **degree <= n:
#    print(2 ** degree)
#    degree+=1
    