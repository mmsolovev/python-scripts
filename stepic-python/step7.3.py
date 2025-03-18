def get_nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(get_nod(15, 121050))
