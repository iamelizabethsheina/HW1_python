
a = int(input())
b = int(input())
#проверка на бесконечность
if a == 0 and b == 0:
    print("inf")
elif a * int(-b/a) + b !=0:
  print("NO")
else:
   print(int(-b / a))