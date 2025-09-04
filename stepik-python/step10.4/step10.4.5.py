cmd = input().lower()
match cmd:
    case 'top':
        print(f'Команда {cmd}')
    case 'bottom':
        print(f'Команда {cmd}')
    case 'right':
        print(f'Команда {cmd}')
    case 'left':
        print(f'Команда {cmd}')
    case _:
        print(f'Неверная команда')
        