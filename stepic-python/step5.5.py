n = str(input())
x = iter(n)
i = 0
while i < len(n):
    print(next(x), end=' ')
    i += 1
