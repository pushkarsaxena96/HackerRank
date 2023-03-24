########################################
# Created by pushkar saxena
##########################################
import random
a = set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
print(a)
print(b)
print("The list of common elements in both the list is as follows:")
common = [x for x in set(a) if x in set(b)]
print(common)
print()

# Using random list
c = random.sample(range(100),10)
d = random.sample(range(100),9)
print(c)
print(d)
print("the List of common elements in both the lists are as follows: ")
common2 = [ y for y in c if y in d]
print(common2)


