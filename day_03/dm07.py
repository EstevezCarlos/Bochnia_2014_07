d = {1: 2, 2: 3, 3: 4}

list_of_items = d.items()
list_of_values = d.values()
d.keys()
d.get(1, 0)


def pseudoget(k, default):
    if k in d:
        return d[k]
    else:
        return default


d.copy()

# d.pop(3)
# print(d.popitem())
# print(d.popitem())
# print(d.popitem())

d.update({'q': 'w'})
print(d)
d.update({1: 7})
print(d)
d.setdefault(1, 8)
d.setdefault(0, 8)
print(d)
d[4] == 5

# print(*d.keys())
# print(*d)

# for k in d.keys():
#     print(k)

# for k in d:
#     print(k)


# list_of_values.append(7)
# print(isinstance(list_of_values, list))
# print(list_of_items)
