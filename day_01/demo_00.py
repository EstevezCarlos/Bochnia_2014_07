# tup = 1, 2, 3 #krotka (tuple)
# tup_2 = (1, 2, 3)
# lis = [1, 2, 3] #lista (list)
# se = {1, 2, 3} #zbiór (set)
# dic = {1:2, 2:3} #słownik (dict)

# set_1 = {'q', 'w', 'e'}
# set_2 = set_1.copy()
# print(set_2)
# removed_element = set_1.pop()
# print(set_2)

# list_1 = [ i*i for i in range(4) ] #wyrażenie listy (list comprehention)
# # x = { i for i in range(3) } #wyrażenie zbioru (set comprehention)
# # x = { i:i*i for i in range(3) } #wyrażenie słownika (dict comprehention)
# gen_1 = ( i for i in range(4) ) #wyrażenie generatora (generator expression)

# for i in zip(list_1, list_1):
#     print(i)

# print('-----------')

# for i in zip(gen_1, gen_1):
#     print(i)


def squares():
    i = 1
    while True:
        yield i**2
        i += 1


gen_1 = squares()
gen_2 = gen_1

for _ in range(10):
    print(next(gen_1))

print("-------------")

for _ in range(10):
    print(next(gen_2))
