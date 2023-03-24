########################################
# Created by pushkar saxena
##########################################
import random
print("Welcome to rock-paper-scissor!")
print("Rock = 1")
print("Paper = 2")
print("Scissor = 3")


def player():
        player1 = input("Player 1 name: ")
        player1choice = int(input("Enter the numeric value next to the options: "))

        player2 = input("Player 2 name: ")
        player2choice = int(input("Enter the numeric value next to the options: "))

        if player1choice == player2choice:
            print("It's a tie")
            a = input("Do you want to play again? (Y/N): ")
            if a=="Y":
                player()
            else : exit()
        elif ((player1choice == 2) and (player2choice==1)) or ((player1choice == 3) and (player2choice == 2)) or ((player1choice == 1) and player2choice == 3):
            print(player1,"is the winner!")
            a = input("Do you want to play again? (Y/N): " )
            if a == "Y":
                player()
            else:
                exit()
        elif ((player2choice == 2) and (player1choice==1)) or ((player2choice == 3) and (player1choice == 2)) or ((player2choice == 1) and player1choice == 3):
            print(player2,"is the winner!")
            a = input("Do you want to play again? (Y/N): " )
            if a == "Y":
                player()
            else:
                exit()
        else :
            print("Invalid choice!")
            a = input("Do you want to play again? (Y/N): ")
            if a == "Y":
                player()
            else:
                exit()

def computer():
    player1 = input("Player 1 name: ")
    player1choice = int(input("Enter the numeric value next to the options: "))
    print()
    player2choice = random.randint(1,3)
    print("computer's choice: ",player2choice)

    if player1choice == player2choice:
        print("It's a tie")
        a = input("Do you wqant to play again? (Y/N): ")
        if a == "Y":
            computer()
        else:
            exit()
    elif ((player1choice == 2) and (player2choice==1)) or ((player1choice == 3) and (player2choice == 2)) or ((player1choice == 1) and player2choice == 3):
        print(player1,"is the winner!")
        a = input("Do you want to play again? (Y/N): ")
        if a == "Y":
            computer()
        else:
            exit()
    elif ((player2choice == 2) and (player1choice==1)) or ((player2choice == 3) and (player1choice == 2)) or ((player2choice == 1) and player1choice == 3):
        print("Computer is the winner!")
        a = input("Do you want to play again? (Y/N): ")
        if a == "Y":
            computer()
        else:
            exit()
    else :
        print("Invalid choice!")
        a = input("Do you want to play again? (Y/N): ")
        if a == "Y":
            computer()
        else:
            exit()

choice = int(input("Whom would you like to play against?"
      "    1. Player  "
      "2. Computer:  "))
if  choice==1:
    player()
elif choice==2:
    computer()















