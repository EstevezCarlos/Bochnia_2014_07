lis = [1, 2, 3, 4]
ran = range(5, 9)
# print(lis)
# print(*lis)
# print(lis[0], lis[1], lis[2], lis[3])
s_1 = {*ran, *lis}

a, *args, b = s_1

print(f"a = {a}, b = {b}, args = {args}")
