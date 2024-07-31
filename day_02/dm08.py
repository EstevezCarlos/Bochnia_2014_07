import atexit


@atexit.register
def add():
    print(a + b)


@atexit.register
def mult():
    print(a * b)


# atexit.unregister(mult)


a = 13
b = 5
