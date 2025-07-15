s1 = '6 10 3 2 1 5'
s2 = '7 10 5 3 6'

set1 = set(map(int, s1.split()))
set2 = set(map(int, s2.split()))

set_int = sorted(list(set1.intersection(set2)))
a = filter(lambda x: x % 2 == 0, set_int)

print(*a)
