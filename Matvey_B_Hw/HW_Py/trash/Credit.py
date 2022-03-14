import math



pip = float(input('Введите сумму, положенную на счет: '))
rir = float(input('Введите годовую процентную ставку: '))
nir = int(input('Введите количество лет: '))
aia = math.pow(p * (1 + r), n)

print('Сумма, полученная через', n, 'лет =', a)
mounth_paid = float(math.ceil(a/36))
print("Ежемесячный платеж: %d " % mounth_paid)
