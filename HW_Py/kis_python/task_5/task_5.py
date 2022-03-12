import math


def main(x):
    _sum = 0
    n = len(x)

    for i in range(1, n+1,1):
        print("i: %d; n: %d" % (i, n))
        v1 = 96 + 97 * math.pow(x[int((n + 1) - round(i / 2))], 2)
        v2 = 97 * x[int((n + 1) - round(i / 2))]
        _sum += 30 * math.pow((v1 + v2), 7)

    return _sum * 6

print(main([0.08, 0.66, 0.33]))
