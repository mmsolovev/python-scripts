tp = input().strip()

if tp == 'RECT':
    def get_sq(a, b):
        s = a*b
        return s
else:
    def get_sq(a):
        s = a**2
        return s
