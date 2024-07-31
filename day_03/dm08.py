from functools import reduce


l = [1, 2, 3, 4, 5]
l[3] = 100
l[1:4] = (10, 20, 30)

l2 = list(map(lambda x: x * 10, l))
print(l2)
l2 = [x * 10 for x in l]
print(l2)

l3 = list(filter(lambda x: bool(x > 5), l))
print(l3)
l3 = [x for x in l if x > 5]
print(l3)

l4 = reduce(lambda x, y: x + y, l)
print(l4)
