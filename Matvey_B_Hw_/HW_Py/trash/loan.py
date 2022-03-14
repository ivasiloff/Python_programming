import math
loan = 2e6;
rate = (5.5/100) / 12;
term = 2;
month = term * 12;
payment = math.floor((loan*rate/(1-math.pow(1+rate,(-1*month))))*100)/100;
print(payment)

