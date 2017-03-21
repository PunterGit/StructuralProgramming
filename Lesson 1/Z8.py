s = input("Введите массив чисел: ")
list = s.split()
j = 0
y = 0

while j < len(list)-1 and not y:
    if (int(list[j]) < 0 and int(list[j+1]) < 0) or (int(list[j]) > 0 and int(list[j+1]) > 0):
        y = 1
    j += 1

if y != 0:
    print("Есть")
else:
    print("Нет")