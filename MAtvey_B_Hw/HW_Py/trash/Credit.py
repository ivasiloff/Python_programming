import math

p = float(input('Введите сумму, положенную на счет: '))
r = float(input('Введите годовую процентную ставку: '))
n = int(input('Введите количество лет: '))
a = math.pow(p * (1 + r), n)

print('Сумма, полученная через', n, 'лет =', a)
mounth_paid = float(math.ceil(a/36))
print("Ежемесячный платеж: %d " % mounth_paid)