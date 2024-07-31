def calc(a, b, oper):
    """
    Function, that calculates operation on two numbers.
    >>> calc(3,5,'+')
    8
    >>> calc(3,5,'-')
    -2
    >>> calc(3,5,'*')
    15
    >>> calc(3,5,'/')
    0.6
    """
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
