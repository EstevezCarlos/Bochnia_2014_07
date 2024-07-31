s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s3 = s1.union(s2)
s4 = s1 | s2
# s1.update(s2)
# s1 |= s2

s5 = s1.intersection(s2)
s6 = s1 & s2
# s1.intersection_update(s2)
# s1 &= s2

s7 = s1.difference(s2)
s8 = s1 - s2
# s1.difference_update(s2)
# s1 -= s2

s9 = s1.symmetric_difference(s2)
s10 = s1 ^ s2
# s1.symmetric_difference_update(s2)
# s1 ^= s2

s1.issuperset(s2)
s1 >= s2
s1.issubset(s2)
s1 <= s2
s1.isdisjoint(s2)


s1 == s2
s1 is s2
