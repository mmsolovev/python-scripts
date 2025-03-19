def get_even(*args):
    lst = []
    for i in args:
        if i % 2 == 0:
            lst.append(i)
    return lst

n = map(int, input().split())
print(*get_even(*n))
