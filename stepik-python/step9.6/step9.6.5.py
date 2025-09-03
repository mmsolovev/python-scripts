lst_in = ['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']
d = {}

for i in lst_in:
    a = i.split(':')
    d[int(a[1])] = a[0]

print(d)


def get_cheep(d):
    a = sorted(d.items())
    return f'{d[a[0][0]]} {d[a[1][0]]} {d[a[2][0]]}'

print(get_cheep(d))
