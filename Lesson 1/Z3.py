print("Введите стороны треугольника:")
a = str(input())
b = str(input())
c = str(input())
print()
a = int(a)
b = int(b)
c = int(c)

if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    print("Треугольник существует")
else:
    print("Треугольника не существует")