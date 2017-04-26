A = bool(1)
B = bool(0)
C = bool(1)

print(A or not(A and B) or C)
print(not A or C and not(B or C))
print((A or B and not C) or A)
