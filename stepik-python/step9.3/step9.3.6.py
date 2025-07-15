s = 'Москва Уфа Вологда Тула Владивосток Хабаровск'

x = list(map(lambda x: x if len(x) > 5 else '-', s.split()))
print(' '.join(x))
