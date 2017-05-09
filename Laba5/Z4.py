import random

def printArr(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

Mx = [[random.randint(0, 9) for j in range(8)] for i in range(7)]

printArr(Mx)

for i in range(0, 8):
    l = 0
    for j in range(0, 7):
        if (Mx[j][i] % 2) != 0:
            l += 1
    print("В ", i+1, " столбце ", l, " нечётных элементов")