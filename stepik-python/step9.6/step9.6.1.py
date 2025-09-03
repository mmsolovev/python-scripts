s = '-2 -1 8 11 4 5 '

lst = list(map(int, s.split()))
tp = tuple(lst)

lst.sort()
tp_lst = tuple(sorted(tp))
print(tp_lst)
