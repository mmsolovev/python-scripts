def tag_func(a, tag='h1', up=True):
    if up:
        tag = tag.upper()
    return f'<{tag}>{a}</{tag}>'

n = input()
print(tag_func(n, 'div'))
print(tag_func(n, 'div', False))
