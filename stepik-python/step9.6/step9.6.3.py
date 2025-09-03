s = '10 5 4 -3 2 0 5 10 3'

lst = list(set(map(int, s.split())))
lst.sort()
print(lst[-1], lst[-2], lst[-3], lst[-4])