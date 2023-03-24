####################################
# Created by Pushkar Saxena
######################################

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []
y = []
for elements in a:
    if elements < 5:
        #printing elements one-by-one.
        print(elements)

# Extra 1 : Adding elements less than 5 to another list
for elements in a:
    if elements < 5:
        x.append(elements)

print(x)

# Extra 2 :
num = int(input("Enter a number: "))
for elements in a:
    if elements < int(num) :
        y.append(elements)

print(y)