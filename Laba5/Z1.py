arr = []
n = 17
otr = 0
kol = 0
S = 0
sr = 0

print("Введите массив из 17 элементов:")
for i in range(0, n):
    arr.append(int(input()))
    if arr[i] < 0:
        otr += abs(arr[i])
        kol += 1

if kol == 0:
    print("Таких нет.")
else:
    sr = otr/kol

    for i in range(0, n):
        if abs(arr[i]) > sr:
            S += arr[i]

    print(S)
