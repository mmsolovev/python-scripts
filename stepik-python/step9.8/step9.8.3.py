lst_in = [1, 2, 6, "a", True, [4, 5], "c", (4, 5)]


def get_even_sum(it):
    return sum(filter(lambda x: type(x) is int and x % 2 == 0, it))


print(get_even_sum(lst_in))
