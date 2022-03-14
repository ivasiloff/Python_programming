"""

    Вариант 3

    a. Написать программу, которая вводит текст и выводит на экран только
    строки, содержащие двузначные числа.

    b. Удалить из строки введенной пользователем лишние (не одинарные)
    пробелы. Реализовать как функцию.

    c. Дана строка. Определить, сколько в ней символов «*», «;», «:».

    d. Определить сколько различных символов входит в заданный текст,
    содержащий не более 100 литер и оканчивающийся точкой.

"""

"""
    Функция для работы с файлами.
    Открытие, чтение, изменение

"""


# T(c)


def count_elements(stroka):
    print(" всего знаков(;): ", stroka.count(';'))
    print(" всего знаков(*): ", stroka.count('*'))
    print(" всего знаков(:): ", stroka.count(':'))


# count_elements("rt rt::;;;;;:;;**T*Y jet y ::;;y YT; ::TY :Y :ty;j ;; :y;y:;;;****")

# T(b)
def make_multi_backspace_to_one(_str):
    _str = _str.split()
    print(' '.join(_str))


# make_multi_backspace_to_one("Hello  world, i am      Matvey ")


# def count_different_characters(_str_1):
# _str_1 = _str_1.split()
# ' '.join(_str_1)
# _size = len(list(_str_1))
# for i in range(_size):
#     if _str_1[i] == _str_1[i + 1]:
#         _str_1.count(_str_1[i])


#

def countDis(str):
    s = set(str)
    print(len(s))
    return s


S = "Hi, i'm Matvey, i'm 20 years old"

print(countDis(S))

def print_strs_with_2_digit_num():
    return 0
