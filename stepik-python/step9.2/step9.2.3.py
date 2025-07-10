import random
from string import ascii_lowercase, ascii_uppercase

random.seed(1)

N = 10
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
a = 0
b = len(chars) - 1


def get_password(symbols, x):
    while True:
        password = ''
        i = 0
        while i < x:
            indx = random.randint(a, b)
            password += symbols[indx]
            i += 1
        yield password


g = get_password(chars, N)
for j in range(1, 6):
    print(next(g))
