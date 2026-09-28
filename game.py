import random

choices = ["rock", "paper", "scissors"]

print ("=== Rock Paper Scissors ===")

while True:
    user = input("\nEnter Rock, Paper, or Scissors (or q to quit): ").lower()

    if user == "q":
        print ("Thanks for playing!")
        break

    if user not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer = random.choice(choices)

    print ("Computer chose:", computer)

    if user == computer:
        print("Result: Draw!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print ("Result: You Win!")

    else:
        print ("Result: You Lose!")
      
