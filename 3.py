n = int(input())
tickets1, tickets10, tickets60 = 0, 0, 0
#вычисление единиц в числе количества поездок
d = n - (n // 10 * 10)
#самый выгодный билет будет на 60 поездок
if 60 >= n > 34:
    tickets60 += 1
#от 60 до бесконечности тоже выгодный билет на 60 поездок
elif n > 60:
    tickets60 += n // 60
#оставшиеся десятки вычитая поездки, которые приобрели с билетами на 60 поездок
    des = n // 10 - n // 60 * 6
    if des * 10 + d <= 34:
        tickets10 += des
        if d > 8:
            tickets10 += 1
        else:
            tickets1 += d
    else:
        tickets60 += 1
else:
    tickets10 += n // 10
    if d > 8:
        tickets10 += 1
    else:
        tickets1 += d
print(tickets1, tickets10, tickets60)