lst_in = [
          'ножницы=100',
          'котелок=500',
          'спички=20',
          'зажигалка=40',
          'зеркальце=50'
         ]

dct = {}

for i in lst_in:
    i.split('=')
    dct[i.split('=')[0]] = int(i.split('=')[1])

a = sorted(dct.items(), key=lambda x: x[1], reverse=True)
print(*[i[0] for i in a])
