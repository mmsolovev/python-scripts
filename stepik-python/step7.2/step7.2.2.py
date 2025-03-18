s = list(map(float, input().split()))


def is_triangle(a, b ,c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False


print(is_triangle(s[0], s[1], s[2]))
