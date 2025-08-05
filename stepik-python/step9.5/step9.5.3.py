b = ['1 2 3 4', '5 6 7 8', '9 8 7 6']

a = [i.split() for i in b]

d1 = zip(*a)

for i in d1:
    print(*i)
    