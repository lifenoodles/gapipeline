def add_vector(a, b):
    return [x + y for (x, y) in zip(a, b)]


def add_scalar(a, b):
    return [x + b for x in a]


def subtract_vector(a, b):
    return [x - y for (x, y) in zip(a, b)]


def subtract_scalar(a, b):
    return [x - b for x in a]


def multiply_scalar(a, b):
    return [x * b for x in a]
