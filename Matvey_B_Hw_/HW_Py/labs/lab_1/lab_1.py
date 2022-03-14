"""
1)Дан массив случайных чисел из а элементов. Вывести на экран
только те элементы этого массива, индексы которых кратны трем.

2)Если 2-е число месяца – четверг, тогда каким днем недели будет n_ное число месяца.

3)Дан массив чисел, заполненный случайным образом. Вывести все
элементы массива, индексы которых не меньше k и не больше n.

4)Пользователь вводит массив чисел n*n элементов. Записать матрицу
в обратном виде (с конца).

5)Вывести двумерный массив n*m, в котором первые элементы числа 3
и 5, а следующие элементы формируется путем сложения предыдущих двух
и деления их на 2.

"""

from random import randint
from random import randint


def ex_1(a):
    nums = [randint(1, 10) for i in range(a)]
    print(nums)
    for e in range(3, len(nums), 3):
        print(nums[e])


def ex_2(n):
    days = ['вт', 'ср', 'чт', 'пт', 'сб', 'вс', 'пн']
    if 0 < n < 32:
        print(days[n % 7])


def ex_3(k, n):
    a = [randint(0, 30) for i in range(0, 10)]
    # k = int(input('От: '))
    # n = int(input('До: '))
    print(a)
    for i, j in enumerate(a):
        if k - 1 < i < n + 1:
            print(j)


def ex_4():
    return 0


def ex_5():
    n = 5
    m = 5
    a = [3, 5]
    for i in range(n * m - 2):
        a.append(round((a[i] + a[i + 1]) / 2, 2))
    res = []
    count = 0
    for i in range(n):
        res.append([])
        for _ in range(m):
            res[i].append(a[count])
            count += 1
    print(*res, sep='\n')
