def my_decorator(func):
    return lambda: func(3)


@my_decorator
def print_x(x):
    for _ in range(x):
        print('x')


print_x()
