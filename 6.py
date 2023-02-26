a = int(input())
b = int(input())
c = int(input())
#находим дискриминант
D = b**2 - 4 * a * c
#если отриц. дискриминант, то выводим нет
if D < 0:
    print("NO")
else:
    #формула по нахождениию корней
    x1 = int(-b + D **0.5 / 2 * a)
    x2 = int(-b - D **0.5 / 2 * a)
if x1 == x2:
    print(x1)
else:
    print(x1,x2)