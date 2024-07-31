from functools import reduce


txt = '12asd345'

result = reduce(
    lambda a, b: (int(a) if isinstance(a, int) or a.isdigit() else 0)
    + (int(b) if b.isdigit() else 0),
    txt,
)


reduce(lambda x, y: x + int(y) if y.isdigit() else x, txt, 0)

print(result)
