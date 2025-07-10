N = 5


def get_sum(total):
    a = [i for i in range(1, total + 1)]
    b = 0
    for j in a:
        b += j
        yield b
