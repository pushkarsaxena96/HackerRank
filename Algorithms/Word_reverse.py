########################################
# Created by pushkar saxena
##########################################

a = input("Enter a string")
def reverse(a):
    spliting_a = a.split()
    new = " ".join(spliting_a[::-1])
    print(spliting_a)
    print(new)

reverse(a)