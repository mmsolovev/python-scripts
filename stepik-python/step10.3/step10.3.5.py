import random

t = 'Петров Иванов Сидоров Балакирев Фридман'
lst_in = t.split()
print(*random.sample(lst_in, 3))
