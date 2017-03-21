x = float(input("Первый день: "))
y = float(input("Пробежал км: "))
d = 1

while x < y:
    d += 1
    x *= 1.1
print(d)
