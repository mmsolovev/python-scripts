digs = list(map(int, input().split()))


def my_func(a, b):
    return a*b


print(my_func(min(digs), max(digs)))
