x = 3
y = 5
z = x + y
s = f'{x} + {y} = {x+y}'
s = '{x} + {y} = {z}'.format(x=x, y=y, z=z)
s = '{} + {} = {}'.format(x, y, z)
s = '{} + {y} = {z}'.format(x, z=z, y=y)

l = [1, 2, 3, 4, 5]
s = str(l)
# s = str(*l)
# s = "".join([str(i) for i in l])
# print(s)

# class Flatened():
#     def __init__(self, collection) -> None:
#         self.collection = collection

#     def __str__(self):
#         return "".join([str(i) for i in self.collection])

# print(Flatened(l))
