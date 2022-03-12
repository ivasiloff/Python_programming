import math


def main(n, a, m, z):
    result_1 = 0
    result_2 = 0

    for i in range(1, a):
        for j in range(1, n):
            result_1 += (7 * math.pow(j, 14) + 70 * math.pow(i, 3))

    for c in range(1, n):
        for k in range(1, m):
            result_2 += ((k / 87) + math.pow(z, 2) + math.pow(c, 6))

    result = result_1 + result_2

    return result
