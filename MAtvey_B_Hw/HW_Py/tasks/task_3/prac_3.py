"""
В одномерном массиве, состоящем из n целочисленных элементов,
вычислить:

1. Произведение элементов с четными номерами.

2. Сумму элементов, расположенных между первым и последним нулевыми
элементами. Преобразовать массив таким образом, чтобы сначала
располагались все положительные элементы, а потом - все отрицательные
(элементы, равные нулю, считать положительными).

"""
from random import *


def even_Odd_product(array, number):
    even = 1
    odd = 1

    for i in range(0, number):
        if i % 2 == 0 and i != 0:
            even += array[i]
        else:
            odd *= array[i]

    print("Even Index Product: ", even)
    print("Odd Index Product: ", odd)


def sortarray(array, number):
    j = 0
    for i in range(0, number):
        if array[i] >= 0:
            temp = array[i]
            array[i] = array[j]
            arr[j] = temp
            j = j + 1
    print(array)


def sum_between_two_numbers(array):
    left_index = array.index(0)
    rigth_index = array[::-1].index(0)

    t_arr = array[left_index: -rigth_index]
    print(sum(t_arr))


#num = int(input())
#arr = [randint(-5, num) for step in range(num)]
arr = [1, 6, 0, -7, 9, 2, 0, 1, ]
num = len(arr)

print(arr)

even_Odd_product(arr, num)
print("тут начинаеться сортировка!")
sortarray(arr, num)
print("тут сробатывает сумма между крайними нулевыми эелментами! ")
sum_between_two_numbers(arr)
