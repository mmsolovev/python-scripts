s = 'house=дом car=машина men=человек tree=дерево'
s_lst = s.split()

tp = tuple((map(lambda x: tuple(x.split('=')), s_lst)))
print(tp)
