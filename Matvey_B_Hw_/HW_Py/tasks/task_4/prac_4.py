"""
Вариант 3

Дана целочисленная прямоугольная матрица. Определить:

1. Количество столбцов, содержащих хотя бы один нулевой элемент.
2. Номер строки, в которой находится самая длинная серия одинаковых
элементов

"""

# m = [[-1, 0, 1],
#     [-1, 0, 1],
#     [0, 1, -1],
#     [1, 0, -1]]
# a = 0
# for i in m:
#     if 0 in i:
#         a = a + 1
# print("строк с нулём",a)



# import random
# def creatArray():
#     r = 0
#     print('Input first index matrix: ')
#     x = int(input())
#     print('Input second index matrix: ')
#     y = int(input())
#     array = []
#     for i in range(x):
#         array.append([])
#         for j in range(y):
#             array[i].append(random.randint(0,100))
#             r += 1
#
# print(creatArray())





mas = [[-6, 0, -3, 7], [-4, 0, 9, -1], [-7, 6, 1, 2]]



for i in mas:
    for j in i:
        print(j, end="  ")
    print("")

#1

print("#1")
counter = 0
#print("len mas[0]: ", len(mas[0]))
#print("len mas: ", len(mas))
for i in range(len(mas[0])):
    for j in range(len(mas)):
        if mas[j][i] == 0:
            counter += 1
            break
print(counter)

#2
print("#2")
counter = 1
best_i = -1
for i in range(len(mas)):
    last = int()
    max_counter = 1
    for j in range(len(mas[i])):
        if mas[i][j] == last:
            counter += 1
        else:
            last = mas[i][j]
            if max_counter < counter:
                max_counter = counter
                counter = 1
                best_i = i
print(best_i)