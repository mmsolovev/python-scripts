def my_func(x):
    l = len(x)
    tpl = (x, l)
    return tpl

cities = input().split()

d = {i: len(i) for i in cities}

a = sorted(d, key=d.get)
print(*a)
