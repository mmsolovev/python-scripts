import re


s = 'abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com'
lst_s = s.split()

a = filter(lambda x: re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', x), lst_s)
print(*a)
