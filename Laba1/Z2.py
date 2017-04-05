import math
t = float(input("Введите t "))
y = float(input("Введите y "))
z = float()

z = (2*t + y*math.cos(t))/math.sqrt(y + 4.831)
print(z)
