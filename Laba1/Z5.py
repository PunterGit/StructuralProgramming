import math

b = 1.3
x = 2.8

a = math.pow(b, 3) + math.log(math.fabs(b))
c = math.pow(a, 2) + math.sqrt(b)
y = math.exp(x) + pow(5.8, c)

print("a =", a, "c =", c, "y =", y)
