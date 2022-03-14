"""
Реализовать интерационную функцию:
"""
import math


m = 6
y = -0.21


def precision_round(number, digits=3):
    power = "{:e}".format(number).split('e')[1]
    return round(number, -(int(power) - digits))




def main(m, y):
    result_1 = 0
    result_2 = 0

    for j in range(1, m + 1):
        v1 = j - 83 * math.pow(j, 2) - 38
        v2 = math.pow((45 * math.pow(j, 3)), 5) + 1
        v3 = 29 * math.pow(j, 2)
        v4 = 90 * math.pow(y, 4)

        result_1 += (93 * round(math.pow(v1, 2)) + v2)
        result_2 += (v3 - v4)

    return precision_round(result_1 - result_2, digits=2)


print(main(m, y))
# try:
#     # assert main(6, -0.21) == 671465.8751645
#     # assert main(6, -0.21) == 6.7 *  math.pow(10, 5)
#     assert main(6, -0.21) == 9.26 * math.pow(10, 19)
#
# except AssertionError:
#     print("TEST ERROR")
#     traceback.print_exc()
# else:
#     print("TEST PASSED")
