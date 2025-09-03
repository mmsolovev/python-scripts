lst_in = ['a', 'b', 1]


def is_string(lst):
    return all(map(lambda x: type(x) is str, lst))

print(is_string(lst_in))
