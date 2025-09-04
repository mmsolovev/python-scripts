t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

match book:
    case _, author, name:
        print('Yes')
    case _, author, name, price:
        print('Yes')
    case _, author, name, price, year:
        print('Yes')
    case _:
        print('No')
