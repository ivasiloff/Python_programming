import math
a = int(input("Введите аргумент: "))

z1 = ((math.sin(2*a) + math.sin(5*a) - math.sin(3*a)) /\
     ((math.cos(a)+1) - 2*math.pow(math.sin(2*a), 2)))
z2 = (2*math.sin(a))

print("z1 = %f" % z1)
print("z2 = %f" % z2)





