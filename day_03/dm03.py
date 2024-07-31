l = [1, 2, 3, 4]

l.append(5)
l.insert(0, 6)
l.insert(-1, 7)
l.insert(len(l), 8)
l.extend('qwerty')
l.remove(4)
x = l.pop(3)
l.clear()
l_x = l.copy()


l2 = l
l3 = l
l3 = l + list('zxcvb')


l.reverse()
l.sort(key=lambda a: a**2)
l.sort(key=abs)


print(l)
print(l2)
print(l3)
