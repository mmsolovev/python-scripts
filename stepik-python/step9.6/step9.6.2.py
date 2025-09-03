d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}


def get_sort(d):
    a = sorted(d, reverse=True)
    return [d[i] for i in a]

print(get_sort(d))