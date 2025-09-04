s = 1

while (d := int(input())) > 0:
    if d % 3 == 0:
        s *= d

print(s)
