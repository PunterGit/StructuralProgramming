n = int(input("Введите количество элементов в массиве "))
m = input("Введите массив: ")
array = m.split()
m = int(array[0])

for i in array:
    print(int(i))
    if int(i) > m:
        m = int(i)
print("Максимальное число: ", m)
