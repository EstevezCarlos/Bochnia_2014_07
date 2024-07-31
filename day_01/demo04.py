import black


def product(a, b, *args, **kwargs):
    result = a * b
    for v in args:
        result *= v
    for v in kwargs.values():
        result *= v
        if True:
            False
    return result


x = 3

print(product(2, 3))
print(product(2, 3, 4, 5, 6))
print(product(c=3, a=1, d=4, b=5))
print(product(1, 5, c=3, d=4))

print('qwe', 'asd', 'zxc', end='\t')
print('qwe', 'asd', 'zxc', end='\t')
print('qwe', 'asd', 'zxc', end='\t')
print('qwe', 'asd', 'zxc', sep='----')
print('qwe', 'asd', 'zxc')
print('qwe', 'asd', 'zxc')
print('qwe', 'asd', 'zxc')
