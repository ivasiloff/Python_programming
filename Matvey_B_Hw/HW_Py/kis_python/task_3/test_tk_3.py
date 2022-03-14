import math


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

    result = result_1 - result_2

    return result
