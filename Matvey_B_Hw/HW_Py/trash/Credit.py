import math



ppppip = float(input('Введите сумму, положенную на счет: '))
rrrrir = float(input('Введите годовую процентную ставку: '))
nnnnir = int(input('Введите количество лет: '))
aaaaia = math.pow(p * (1 + r), n)

print('Сумма, полученная через', n, 'лет =', a)
mounth_paid = float(math.ceil(a/36))
print("Ежемесячный платеж: %d " % mounth_paid)
