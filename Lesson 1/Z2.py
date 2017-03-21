print("Введите 3 числа:")
a = str(input())
b = str(input())
c = str(input())

a = int(a)
b = int(b)
c = int(c)
if a > b and a > c:
    print("Наибольшее число ", a)
elif b > c:
    print("Наибольшее число ", b)
else:
    print("Наибольшее число ", c)
