l = [2, 3, 4, 2, 5, 7, 2]

x = l.index(2)
print(x)
print(l.index(2, x + 1))

print(l.count(2))

l2 = l + l
l3 = [*l, *l]


r1 = range(0, 3, 1)
r2 = range(13, 51, 3)
r3 = range(0, 5, 1)

r3 = list(r1) + list(r2)

print(l[3:66:2])
s = slice(3, 66, 2)
print(l[s])
range(3, 6)

print(l[::-1])
