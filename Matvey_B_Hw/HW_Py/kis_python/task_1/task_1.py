import math


def main(x):
    x1 = math.pow(math.ceil(x), 6)
    x2 = math.pow(math.cos(x), 3)
    x3 = (26*(math.pow(x, 3))-97*x)
    x4 = math.pow(x, 5)
    x5 = math.pow(x, 12)
    x6 = 29*(math.pow(x, 3))
    return (x5-x6)-((x1-x2)/(x4-(math.pow(x3, 2))))