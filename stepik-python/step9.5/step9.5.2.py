b = ['1 2 3 4 5 6', '3 4 5 6', '7 8 9', '9 7 5 3 2']
a = [i.split() for i in b]

d1 = zip(*a)
d2 = zip(*d1)

for i in d2:
    print(*i)
