from itertools import count, repeat, cycle

gen_1 = ( i*i for i in cycle([0,5,10]) )

print(next(gen_1))
print(next(gen_1))
print(next(gen_1))
print(next(gen_1))
print(next(gen_1))
print(next(gen_1))


def create_gen():
    i = 0
    while True:
        i+=1
        yield i
gen = create_gen()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
