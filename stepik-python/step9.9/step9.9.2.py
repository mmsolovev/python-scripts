t = '8.2 -11.0 20 3.4 -1.2'
lst_in = map(float, t.split(' '))

print(any(map(lambda x: x < 0, lst_in)))
