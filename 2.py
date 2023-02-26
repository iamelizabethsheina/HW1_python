x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
#проверяем на 3 четветь точки
if x1<0 and y1<0 and x2<0 and y2<0:
    print("YES")
#проверяем на 4 четверть точки
elif x1>0 and y1<0 and x2>0 and y2<0:
    print ("yes")
#проверяем на 1 четверть точки
elif x1>0 and y1>0 and x2>0 and y2>0:
    print ("yes")
#проверяем на 2 четверть точи
elif x1<0 and y1>0 and x2<0 and y2>0:
    print("yes")
else:
    print("no")