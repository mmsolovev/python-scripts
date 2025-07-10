import random
from string import ascii_lowercase, ascii_uppercase

random.seed(1)

N = 8
chars = ascii_lowercase + ascii_uppercase
a = 0
b = len(chars) - 1


def get_mail(symbols, x):
    while True:
        mail = ''
        i = 0
        while i < x:
            indx = random.randint(a, b)
            mail += symbols[indx]
            i += 1
        yield f'{mail}@mail.ru'


g = get_mail(chars, N)
for j in range(1, 6):
    print(next(g))
