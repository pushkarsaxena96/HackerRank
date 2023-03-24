########################################
# Created by pushkar saxena
##########################################

number  = int(input("enter the number: "))
i = 1
fib = []
if number == 0:
    fib=[]
elif number == 1:
    fib=[1]
elif number == 2 :
    fib=[1,1]
elif number > 2 :
    fib = [1,1]
    while i < (number-1) :
        fib.append(fib[i]+fib[i-1])
        i=i+1
else :
    print("Invalid Input!")

print("Fibonacci Series :",fib)
