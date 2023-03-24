########################################
# Created by pushkar saxena
##########################################
repeat="Y"
while (repeat!="N"):
    number = int(input("Enter the number: "))
    count = 0
    for x in range(1,number,1):
        if number % x == 0:
            count=count+1

    if count > 2:
        print("It is not a prime number")
    elif count <= 2:
        print("It is a prime number")
    repeat = input("Do you want to try again? (Y/N) ")
