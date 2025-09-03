t = '3 3 3 2 3 3'
lst_in = map(int, t.split(' '))

if any(map(lambda x: x < 3, lst_in)):
    print('отчислен')
else:
    print('учится')
