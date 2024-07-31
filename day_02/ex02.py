"""
Dekoratory wykonujące dekorowaną funkcję 5 razy.
>>> check_repeat_five()
sssss
>>> check_repeat_five_better('S')
('S', 'S', 'S', 'S', 'S')
"""


def repeat_five(fun):
    def result():
        fun()
        fun()
        fun()
        fun()
        fun()

    return result


@repeat_five
def check_repeat_five():
    print('s', end='')


def repeat_five_better(fun):
    def result(*args, **kwargs):
        a = fun(*args, **kwargs)
        b = fun(*args, **kwargs)
        c = fun(*args, **kwargs)
        d = fun(*args, **kwargs)
        e = fun(*args, **kwargs)
        return a, b, c, d, e

    return result


@repeat_five_better
def check_repeat_five_better(txt):
    return txt
