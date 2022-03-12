import math

def main(x):
    if x < 139:
        return 55 * (math.pow(48*x, 2))
    elif 139 <= x and x < 199:
        return math.pow(x, 6) - 95 * (math.pow(x-18), 3) - 91*math.pow(math.sin(x), 5)
    elif (199 <= x and x < 224):
        return math.pow(x, 6)
    elif (224 <= x and 244):
        x >= 244