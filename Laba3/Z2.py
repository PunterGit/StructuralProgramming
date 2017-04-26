import math
n = int(input("Введите n "))
k = n

while k > 0:
    Q = (pow(-1, k) * (k - 7)) / math.factorial(k + n)
    k -= 1
print(Q)
