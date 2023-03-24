########################################
# Created by pushkar saxena
##########################################

y = int(input("Enter a number"))
x = range(2,y+1)
z = []
for elements in x :
    if y % elements ==0 :

        #Printing elements
        print("Divisor = ",elements)
        # Adding diviors to list z
        z.append(elements)

print(z)

