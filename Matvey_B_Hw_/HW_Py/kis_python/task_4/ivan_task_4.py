import math


def main(n):
    if n == 0:
        return -0.84
    elif n >= 1:
        return 1 + \
               (math.cos(53 * math.pow(main(n - 1), 2) - main(n - 1) - 25))/7
