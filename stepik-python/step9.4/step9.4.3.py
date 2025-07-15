s = '8 11 0 -23 140 1'
lst_n = s.split()

n = filter(lambda x: len(x) == 2 if x[0] != '-' else len(x) == 3, lst_n)
print(*n)
