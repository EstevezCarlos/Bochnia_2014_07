def scrape(lis, value):
    result = lis.count(value)
    for _ in range(result):
        lis.remove(value)
    return result


def scraped(lis, value):
    return list(filter(lambda item: item != value, lis))


def scraped_2(lis, value):
    return [item for item in lis if item != value]


print(' --- scrape --- ')
l1 = [1, 2, 3]
print(l1)
print(scrape(l1, 2))
print(l1)

print(' --- scraped --- ')
l2 = [1, 2, 3]
print(l2)
print(scraped(l2, 2))
print(l2)

print(' --- scraped_2 --- ')
l3 = [1, 2, 3]
print(l3)
print(scraped_2(l3, 2))
print(l3)
