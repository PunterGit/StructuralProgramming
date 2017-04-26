m = int(input("Введите m "))
n = int(input("Введите n "))
s = 0
while m <= n:
    s += pow(m, 2)
    m += 1

print(s)
