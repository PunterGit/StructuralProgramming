N = int(input("Введите число N "))
L = bool(False)

if (N % 2) == 0:
    if (N % 3) != 0:
        if (N % 7) == 0:
            L = True
        else:
            L = False
    if L == 0:
        if (N % 5) != 0:
            if (N % 4) != 0:
                L = True
    if L == 0:
        if (N % 8) == 0:
            if (N % 11) == 0:
                L = True

print(L)
