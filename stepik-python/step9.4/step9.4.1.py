s = 'Тула Ульяновск Хабаровск Владивосток Омск Уфа'

a = filter(lambda x: len(x) > 5, s.split())
for i in range(1, 4):
    print(next(a), end=' ')
