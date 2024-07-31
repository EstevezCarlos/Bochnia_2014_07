try:
    x = int(input('Podaj liczbę: '))

except Exception as error:
    print(error)


def my_error(txt: str):
    return ValueError(f'{txt} Cannot be zero')


# X_ERROR = ValueError('x Cannot be zero')

if x == 0:
    raise my_error('x')
