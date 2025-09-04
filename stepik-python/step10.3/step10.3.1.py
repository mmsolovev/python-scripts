import random


t = '-4 5'
lst_in = map(float, t.split())

print(round(random.uniform(*lst_in), 2))
