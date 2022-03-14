import math



pipa = float(input('Введите сумму, положенную на счет: '))
rira = float(input('Введите годовую процентную ставку: '))
nira = int(input('Введите количество лет: '))
aiaa = math.pow(p * (1 + r), n)

print('Сумма, полученная через', n, 'лет =', a)
mounth_paid = float(math.ceil(a/36))
print("Ежемесячный платеж: %d " % mounth_paid)
