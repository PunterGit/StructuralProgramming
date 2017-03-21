y = int(input("Введите год "))
print()

if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
  print("Год високосный")
else:
  print("Год не високосный")