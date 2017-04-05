import math
x = float(input("Введите x "))
y = float(input("Введите y "))
U = float()

U = (math.exp(math.pow(x, 3)) + (math.pow(math.cos(x - 4), 2)))/(math.atan(x) + 5.2 * y)
print(U)
