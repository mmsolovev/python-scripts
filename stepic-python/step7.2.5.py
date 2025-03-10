def is_odd(a):
    if a % 2 != 0:
        return a


lst_d = list(map(int, input().split()))
lst = [i for i in lst_d if is_odd(i)]
print(*lst)
