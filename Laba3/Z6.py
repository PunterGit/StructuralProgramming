import math

n = int(input("Введите n "))
x = int(input("Введите x "))
s = 1

for i in range(1, n):
    s += (math.cos(i * x)) / math.factorial(i)

print(s)
