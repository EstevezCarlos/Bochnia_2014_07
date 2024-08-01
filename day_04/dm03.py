gen = (i for i in range(6))
lis = [i for i in range(6)]

print('--- generator ---')
for i,j, k in zip(gen, gen, gen):
    print(i,j,k)

print('--- lista ---')
    
for i,j in zip(lis, lis):
    print(i,j)

gen = (i for i in range(6))
print(next(gen))
print(next(gen))
print(next(gen))