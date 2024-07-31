"""
Dekorator konwertujący na inty, wszystkie argumenty
>>> add('3','5')
8
"""


def all_ints(fun):
    def result(*args, **kwargs):
        args_2 = [int(v) for v in args]
        kwargs_2 = {k: int(v) for k, v in kwargs}
        return fun(*args_2, **kwargs_2)

    return result


@all_ints
def add(a, b):
    return a + b
