import math


def main(y):
    _sum = 0
    n = len(y)
    for i in range(1, n + 1):
        v1 = 31 * y[int((n-1) + 1 - math.ceil(i / 4))]
        v2 = 11 * math.pow(y[int((n-1) + 1 - math.ceil(i / 2))], 3)
        _sum += math.pow(v1 + 1 + v2, 4)
    return _sum
