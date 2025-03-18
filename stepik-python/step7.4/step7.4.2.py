def check_password(a, b='$%!?@#'):
    if len(a) > 8:
        for i in b:
            if i in a:
                return True
    return False

