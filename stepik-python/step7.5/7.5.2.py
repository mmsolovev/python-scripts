def get_biggest_city(*args):
    biggest = ''
    for i in args:
        if len(i) > len(biggest):
            biggest = i
    return biggest

n = map(str, input().split())
print(get_biggest_city(*n))
