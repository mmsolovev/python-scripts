t = '2 4 6 8 22 56'
lst_in = map(int, t.split(' '))

print(all(map(lambda x: x % 2 == 0, lst_in)))
