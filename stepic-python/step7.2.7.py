def is_large(s):
    return len(s) >= 6

cities = input().split()
lst = [i for i in cities if is_large(i)]

print(*lst)
