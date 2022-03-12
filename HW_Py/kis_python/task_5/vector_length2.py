import math


def main(x):
    _sum = 0
    n = len(x)

    # _sum += 30 * (96 + 97 * x[1] ** 2 + 97 * x[1]) ** 7
    # _sum += 30 * (96 + 97 * x[2] ** 2 + 97 * x[2]) ** 7
    # _sum += 30 * (96 + 97 * x[2] ** 2 + 97 * x[2]) ** 7

    for i in range(1, n + 1):
        # print(i)
        # print(i, int((n-1) + 1 - math.ceil(i / 2.0)))
        _sum += 30 * (96 +
                      97 * x[int((n - 1) + 1 - math.ceil(i / 2.0))] ** 2 +
                      97 * x[int((n - 1) + 1 - math.ceil(i / 2.0))]) ** 7
    return _sum * 6


print(main([-0.5, 0.08, -0.52]))
print(main([0.08, 0.66, 0.33]))
