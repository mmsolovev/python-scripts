def tag_func(a, tag='h1'):
    return f'<{tag}>{a}</{tag}>'

n = input()
print(tag_func(n))
print(tag_func(n, 'div'))
