s = float(input("Введите стоимость покупки "))

if (s > 500) and (s <= 1000):
    s = s - s * 0.05
else:
    if s > 1000:
        s = s - s * 0.1

print(s)
