def get_data(value):
    match value:
        case int(value):
            return value
        case float(value):
            return value
        case str(value):
            return value
    return None

print(get_data([1, 2, 3]))
