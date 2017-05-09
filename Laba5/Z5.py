import random

def printArr(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

C = []
M = int(input("Введите M "))
N = int(input("Введите N "))

Mx = [[random.randint(0, 9) for j in range(N)] for i in range(M)]
printArr(Mx)
B = abs(float(input("Введите B ")))

for i in range(0, M):
    for j in range(0, N):
        if Mx[i][j] > B:
            C.append(Mx[i][j])

print("Массив C: ", C)
print("Всего элементов: ", len(C))
