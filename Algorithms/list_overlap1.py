########################################
# Created by pushkar saxena
##########################################

print("For random list")
import random
r1 = set(random.sample(range(100),12))
r2 = set(random.sample(range(100),13))
print(r1)
print(r2)
# In one line
ran_common = [x for x in set(r1) if x in set(r2)]
print(ran_common)
print()
print()

print("for pre-defined list")

a = set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
d = []
print(a)
print(b)
print("In one-line")
c = [x for x in set(a) if x in set(b)]
print(c)
print()
print("Using loop")
for x in a and b :
    if x in a and b :
        d.append(x)
print(d)