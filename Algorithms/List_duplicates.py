########################################
# Created by pushkar saxena
##########################################

a = [1,1,2,3,4,5,5,6,7,8]
print(a)
b = []

def dup(a):
    for x in a:
        if x not in b:
            b.append(x)

dup(a)
print(b)
