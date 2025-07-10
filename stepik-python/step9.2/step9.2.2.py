N = 7


def balak_seq(max_len):
    a, b, c = 1, 1, 1
    for i in range(1, N + 1):
        yield a
        a, b, c = b, c, a + b + c


g = balak_seq(N)
for j in range(N):
    print(next(g), end=' ')
