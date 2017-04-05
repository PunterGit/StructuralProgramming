import math

x0 = float(input("Введите x0 "))
y0 = float(input("Введите y0 "))
z0 = float(input("Введите z0 "))

a = 4
b = -2
c = -5
d = -5

p1 = math.fabs(a*x0 + b*y0 + c*z0 + d)/math.sqrt(math.pow(a, 2) + math.pow(b, 2) + math.pow(c, 2))
print(p1)

a = 2
b = -1
c = 3
d = 1

p2 = math.fabs(a*x0 + b*y0 + c*z0 + d)/math.sqrt(math.pow(a, 2) + math.pow(b, 2) + math.pow(c, 2))

print(p2)
