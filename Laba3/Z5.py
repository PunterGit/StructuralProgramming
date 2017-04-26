n = int(input("Введите натуральное n "))
tf = False
i = 1

def print_factors(x):
    s = 0
    for j in range(1, x):
        if x % j == 0:
            s = s + j

    if s == x:
        tf = True
    else:
        tf = False
    return tf

while i < n:
    if print_factors(i) == True:
        print(i)
    i += 1
