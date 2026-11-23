
import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

player = input("Choose rock, paper, or scissors: ").lower()

print("Computer chose:", computer)
print("You chose:", player)

if player == computer:
    print("It's a draw!")

elif player == "rock" and computer == "scissors":
    print("You win!")

elif player == "paper" and computer == "rock":
    print("You win!")

elif player == "scissors" and computer == "paper":
    print("You win!")

elif player in choices:
    print("Computer wins!")

else:
    print("Invalid choice!")
