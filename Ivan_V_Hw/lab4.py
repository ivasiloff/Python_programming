import random


def matrix1():
    matrix = [[1,-1,3],[5,4,5],[5,2,-2]]

    for i in matrix:
        flag = True
        sum = 1
        for g in i:
            sum *= g
            if g<0:
                flag = False
        if flag:
            print(i,sum)


def matrix2():
    a = []
    n = int(input('n = '))
    for i in range(n):
        b = []
        for j in range(n):
            b.append(random.randint(0, 100))
            print('{:5d}'.format(b[j]), end='')
        a.append(b) #добавляем в лист массив из чисел (строка - [1, 2, 3])
        print()
    max = 0
    for k in range(-n+1, n):
        sum = 0
        for j in range(n):
            if(j+k >= 0) and (j+k <n):
                sum += a[j+k][j]
                if j+k == 1:
                    max = sum
                elif sum > max:
                    max = sum
        print(str(j+k) + " = ", sum)
    print(str(max))

if __name__ == '__main__':
    matrix1() #complete
    matrix2() #complete