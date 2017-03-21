x = int(input("Введите число "))
if x == 0:
    print("0 не является натуральным числом")
elif x < 0:
    x *= -1
else:
    pass
for i in range(1, x):
    if x % i == 0:
        print(i)
