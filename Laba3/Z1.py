N = int(input("Введите N > 0 "))
p = float(1)
if N <= 0:
    print("Вы ввели отрицательное N")
else:
    while N > 0:
        p = (p * (1 / N))
        N = (N - 1)
    print("Произведение = ", 2 * p)

