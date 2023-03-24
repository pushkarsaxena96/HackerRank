number = int(input("Enter a number "))
if number % 2 ==0:
    print(number,"is even")
else :
    print(number,"is odd")

if number % 4 == 0:
    print (number,"is divisible by 4")
else :
    print (number,"is not divisible by 4")

num = int(input("Enter another number "))
check = int(input("Enter the number to check divisibility "))
if num%check ==0:
    print (num,"is divisible by", check)
else :
    print (num,"is not divisible by", check)



