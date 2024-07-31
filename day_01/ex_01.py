def week_generator():
    while True:
        for day in ["Pn", "Wt", "Śr", "Cz", "Pt", "Sb", "Nd"]:
            yield day


week_1 = week_generator()

for _ in range(10):
    print(next(week_1))
