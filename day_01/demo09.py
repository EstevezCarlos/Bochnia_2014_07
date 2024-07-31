x = 0
import time

if x == 0:
    raise ValueError('"x" nie może być zerem.')

try:
    print(3/x)
except ZeroDivisionError as error:
    print(f'x jest zerem: {error}')
except Exception as error:
    print(f'nieznany błąd: {error}')
finally:
    print('Do widzeniea')


# def tryhard(function):
#     for _ in range(10):
#         try:
#             function
#         except Exception as error:
#             pass
#         time.sleep(1)
#     raise ConnectionError('Cannot connect to something 1')

