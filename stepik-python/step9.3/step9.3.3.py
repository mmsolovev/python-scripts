import sys

# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['8 11 -5', '3 4 10', '-1 -2 3', '-4 5 6']

s = map(lambda x: x.split(), lst_in)

lst2D = []

for i in range(1, len(lst_in) + 1):
    x = map(int, next(s))
    lst2D.append(list(x))

print(lst2D)