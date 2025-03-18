def get_rect_value(a, b, tp=0):
    return a * b if tp else (a + b) * 2

print(get_rect_value(2, 3))
