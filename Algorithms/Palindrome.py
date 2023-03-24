########################################
# Created by pushkar saxena
##########################################

string = input("Enter a string: ")
if string == string[::-1] :
    print("This is a palindrome")
else :
    print("This is not a palindrome")

print()
#using loops
def reverse(string):
    for a in range(0,int(len(string)/2)):
        if string[a]!= string[len(string)-a-1]:
            return False
            break

if reverse(string)==False:
    print("This is not a palindrome")
else :
    print("This is a palindrome")


