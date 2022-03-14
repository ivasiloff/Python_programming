import math


def main(y):
    y11 = math.pow((math.pow(y, 3) - y), 5)
    y12 = math.pow(math.atan(1 - 53 * y), 3)

    y21 = math.pow((18 * y), 4)
    y22 = (40 * (math.pow(y, 3)))

    y31 = math.pow(y, 6)
    y32 = (12 * y + 8 * (math.pow(y, 3)))
    math.pow(math.atan(y32), 5)

    math.pow(y, 3)
    y5 = math.pow(math.log10(math.pow(y, 3)), 6)

    if y < 67:

        return y11 - y12

    elif 67 <= y < 122:

        return y21 - y22 - 7 * y

    elif 122 <= y < 138:
        return y31 + math.pow(math.atan(y32), 5)

    elif y >= 138:
        return 65 * y5

    else:
        return 1
