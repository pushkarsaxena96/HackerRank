########################################
# Created by pushkar saxena
##########################################

import random

number = random.randint(1,9)
guess = 0


print("Welcome to the guessing game!")
answer=0

while answer!=number or answer == "exit" or answer == "EXIT" or answer == "Exit":
    answer = int(input("Guess a number between 1 and 9. Let's see if you can guess the correct number"))

    if (answer== "exit"):
        print("Thankyou for playing")
        break

    elif (answer == number):
        guess=guess+1
        print("congratulations! You guessed it right in",guess,"tries!")

    elif (answer != number):
        guess=guess+1
        print("OOPS! Try again")

