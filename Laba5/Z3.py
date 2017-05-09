A = []
B = []

print("Введите первый массив: ")
for i in range(0, 7):
    A.append(float(input()))
print("Введите второй массив: ")
for i in range(0, 9):
    B.append(float(input()))

C = A + B
m = len(C) - 1
while m > 0:
    for i in range(m):
        if C[i] > C[i+1]:
            x = C[i]
            C[i] = C[i+1]
            C[i+1] = x
    m -= 1

print("Третий массив: ")
for i in range(0, len(C)):
    print(C[i])