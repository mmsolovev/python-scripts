lst_in = ['зонт=1000', 'палатка=10000', 'спички=22', 'котелок=543']

tp = tuple((map(lambda x: tuple(x.split('=')), lst_in)))

lst_out = filter(lambda x: x if int(x[1]) > 500 else False, tp)

for i in tuple(lst_out):
    print(i[0], end=' ')
