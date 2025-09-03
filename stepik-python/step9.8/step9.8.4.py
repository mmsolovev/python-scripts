lst_in = [1, 2, 6, "a", True, [4, 5], "c", (4, 5)]


def get_list_dig(lst):
    return [*filter(lambda x: type(x) in (int, float), lst)]


print(get_list_dig(lst_in))
