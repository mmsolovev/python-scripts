lst_in = [1, 2, 3, "a", True, [4, 5], "c", (4, 5)]


def get_sum(a):
    if sum(filter(lambda x: type(x) is int, lst_in)):
        return sum(filter(lambda x: type(x) is int, lst_in))
    else:
        return 0


print(get_sum(lst_in))
