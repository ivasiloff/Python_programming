import math


def main(n):
    if n == 0:
        return 0.82
    elif n >= 1:
        return math.pow((math.pow(main(n - 1), 2) / 37), 3) \
               + math.tan(main(n - 1)) + 1


print(main(4))
# import math
#
#
# def main(n):
#     v1 = math.pow((math.pow(main(n - 1), 2) / 37), 3)
#     v2 = math.tan(main(n - 1)) + 1
#     if n == 0:
#         return 0.82
#     elif n >= 1:
#         return v1 + v2
#
#
# print(main(4))
