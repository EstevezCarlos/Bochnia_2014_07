def calc(a, b, oper):
    dic = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': (lambda a, b: a / b) if b != 0 else float('inf'),
    }
    if oper in dic:
        return dic[oper](a, b)
    else:
        raise ValueError(
            "Uknown operatr, only '+', '-', '/', '*' are availible."
        )


def calc_2(a, b, oper):

    dic = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': (lambda a, b: a / b) if b != 0 else float('inf'),
    }

    def raise_err(*args):
        raise ValueError(
            "Uknown operatr, only '+', '-', '/', '*' are availible."
        )

    return dic.get(oper, raise_err)(a, b)


print(calc(3, 0, '/'))
