a = list(map(int, '7 6 4 2 6 7 9 10 4'.split()))
b = list(map(int, '-4 5 10 4 5 65'.split()))

a.sort()
b.sort(reverse=True)


d1 = zip(a, b)
n = map(lambda x: x[0]+x[1], d1)

print(*n)
