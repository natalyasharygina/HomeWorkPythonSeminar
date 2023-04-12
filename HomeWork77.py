# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и 
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows +1):
#         for j in range(1, num_columns + 1):
#             if i != 1 and j != 1:
#                 print(operation(j, i), end="\t")
#             elif i == 1:
#                 print(j, end= "\t")
#             else:
#                 print(i, end = "\t")
#         print()  
# print_operation_table(lambda x, y: x + y)                        

# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# def winnie(line_poem: str) -> str:
#     line_poem = line_poem.lower().split()
#     letters = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
#     for i in range(len(line_poem)):
#         count = 0
#         for j in line_poem[i]:
#             if j in letters:
#                 count += 1
#         line_poem[i] = count
#     if len(set(line_poem)) == 1:
#         return 'Парам пам-пам'
#     return 'Пар парам'   
# song = input('Ведите часть песни: ')    
# print(winnie(song))