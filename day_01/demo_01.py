import itertools

itertools.count(10, 2)
range(10, 20, 2)

rep = itertools.repeat("qwe")
# print(list(rep))

week = itertools.cycle(["Pn", "Wt", "Śr", "Cz", "Pt", "Sb", "Nd"])

endless = (i**2 for i in itertools.count() if i % 2 == 0 and len(str(i)) % 2 == 0)
endless = (i**2 for i in itertools.count(0, 2))

for _ in range(10):
    print(next(week))
