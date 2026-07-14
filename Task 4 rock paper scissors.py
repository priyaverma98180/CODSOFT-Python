import random 
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
print("===== ROCK PAPER SCISSORS GAME =====")
while True:
    user = input("\nEnter Rock, Paper or Scissors: ").lower()
    if user not in choices:
        print("Invalid Choice! Please try again.")
        continue
    computer = random.choice(choices)
    print("You chose:", user)
    print("Computer chose:", computer)
    if user == computer:
        print("It's a Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
        user_score += 1
    else:
        print("Computer Wins!")
        computer_score += 1
    print("\nScore")
    print("You:", user_score)
    print("Computer:", computer_score)
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\n===== FINAL SCORE =====")
        print("You:", user_score)
        print("Computer:", computer_score)
        if user_score > computer_score:
            print("Congratulations! You Won the Game.")
        elif computer_score > user_score:
            print("Computer Won the Game.")
        else:
            print("The Game Ended in a Tie.")
        print("Thank You for Playing!")
        break