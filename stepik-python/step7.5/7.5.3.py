def get_data_fig(*args, **kwargs):
    lst = ['tp', 'color', 'closed', 'width']
    n = []
    for i in lst:
        if i in kwargs:
            n.append(kwargs[i])

    return (sum(args),) + tuple(n)


n = map(int, input().split())
print(get_data_fig(*n, tp=True, color=12, closed=False, wigth=11.0))
