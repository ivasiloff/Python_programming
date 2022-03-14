import random

def arrays_1():
    n = int(input())
    array = [random.randint(0, n) for x in range(n)]
    sum = 0
    for i in range(array.__len__()):
        print(array[i])
        if (i % 2 != 0 and i != 0):
            sum = sum + array[i]
    print (sum)


def arrays_2():
    n = int(input())
    array = [0] * n
    sum = 0

    for i in range(n):
        array[i] = float(input())

    first = 0
    second = n-1
    for x in range(0,n,1):
        if(array[x]<0):
            first = x
            break
    for y in range(n-1,-1,-1):
        if(array[y]<0):
            second = y
            break

    for i in range(first+1,second,1):
        sum += array[i]
    print(sum)

    array_id = []
    for i in range(n):
        if(abs(array[i])<1):
            array_id.append(i)

    for i in array_id:
        array.pop(i)
        array.append(0)

    print(array)



if __name__ == '__main__':

    arrays_1() #complete - «Одномерные массивы»
    arrays_2() #complete - «Одномерные массивы»


