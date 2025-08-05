a = list(map(int, '-7 8 11 -1 3'.split()))
b = list(map(int, '1 2 3 4 5 6 7 8 9 10'.split()))

d1 = zip(a, b)
n = map(lambda x: x[0]*x[1], d1)

print(next(n), next(n), next(n))
