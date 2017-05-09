import random

def printArr(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

Mx = [[random.randint(0, 9) for j in range(10)] for i in range(5)]

printArr(Mx)

Col = 0

print("Номера монотонно убывающих столбцов: ")
for i in range(0, 10):
    l = 0
    for j in range(0, 4):
        if Mx[j][i] >= Mx[j + 1][i]:
            l += 1
        if l == 4:
            Col += 1
            print(i + 1)

print(Col, " столбцов монатонно убывают")
