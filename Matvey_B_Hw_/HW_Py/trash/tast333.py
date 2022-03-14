
import math

def distance(x1,y1, x2, y2 ):
    return math.sqrt((x1-x2)*(x1-x2) + (y1 - y2)*(y1 - y2))

def geron(x1,y1, x2, y2, x3, y3):
    a = distance(x1,y1, x2, y2)
    b = distance(x1,y1, x3, y3)
    c = distance(x3,y3, x2, y2)
    p =(a + b + c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

if __name__ == '__main__':
    x1 = int(input('x1= '))
    y1 = int(input('y1= '))
    x2 = int(input('x2= '))
    y2 = int(input('y2= '))
    x3 = int(input('x3= '))
    y3 = int(input('y3= '))
    s = geron(x1, y1, x2, y2, x3, y3 )
    x4 = int(input('x4= '))
    y4 = int(input('y4= '))
    s124 = geron(x1, y1, x2, y2, x4, y4)
    s234 = geron(x2, y2, x3, y3, x4, y4)
    s134 = geron(x1, y1, x3, y3, x4, y4)
    s = geron(x1, y1, x2, y2, x3, y3)
    eps = 1e-10

    print("Внутри" if math.fabs(s-(s124+s234+s134))<eps else "Вне")
    print(s)
    print(s124 + s234 + s134)





