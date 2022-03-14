"""
тестовые: 1 10 1 0.001

"""


def factorial(j=int()):
    if j == 0:
        return 1
    else:
        return j * factorial(j - 1)


X_start = float(input())
X_end = float(input())
dx = float(input())
e = float(input())

f = int(X_start)

k = 1
while e < 1:
    e = e * 10
    k += 1

i = 0
k = k * 10
while f <= X_end:
    print(int(f), ')', end=" ")
    print(round((pow(f, i) / factorial(i) * k)) / k)
    i += 1
    f = f + dx
