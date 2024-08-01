l = [1,2,3,4,5]
s = ''.join([str(i) for i in l])


def my_finction():
    my_long_string = """
    Litwo, ojcyzno moja
    Ty jesteś jak zdrowie
    ...
    """
    return my_long_string.replace('    ','').strip().split('\n')


print(my_finction())