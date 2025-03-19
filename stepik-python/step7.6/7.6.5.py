import sys

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))

menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# здесь продолжайте программу (используйте список lst_in и menu)

lst_in = ['Города=about-cities', 'Машины=read-of-cars', 'Самолеты=airplanes']

d = {i: j for i, j in [i.split("=") for i in lst_in]}
menu = {**menu, **d}
print(menu)
