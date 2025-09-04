def get_data(value):
    match value:
        case int() as command if command > 0:
            return value
        case float() as command if -100.0 <= command <= 100.0:
            return command
        case str():
            return value
    return None

print(get_data(-1))