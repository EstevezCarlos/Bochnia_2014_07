from functools import partial

dic = {"q": 1, "w": 2, "e": 3}

print_dict = {
    "sep": "---",
    "end": "\n\n\n",
}
# for k, v in dic.items():
#     print(f'klucz = {k}, wartość = {v}')

print(1, 2, 3, sep="---", end="\n\n\n")

print(1, 2, 3, **print_dict)
print(1, 2, 3, **print_dict)
print(1, 2, 3, **print_dict)

default_print = partial(print, sep="---", end="\n\n\n")

default_print(1, 2, 3)
default_print(1, 2, 3)
default_print(1, 2, 3)
