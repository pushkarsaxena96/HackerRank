import datetime
now = datetime.datetime.now()
name = input("Enter Your Name")
age = int(input("Enter Your age"))
print("Your name is",name)
print("Your age is",age)
#print(now.year)
YearOfTurning100 = (100-age) + int(now.year)
print("You will turn 100 in", YearOfTurning100)
