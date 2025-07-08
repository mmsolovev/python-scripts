a = 3

abs_lst = [abs(i) for i in range(-a, a + 1)]
cube_lst = [str(i**3) for i in abs_lst]

print(' '.join(cube_lst[:4]))
