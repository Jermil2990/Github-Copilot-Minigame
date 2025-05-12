# write 'hello world' to the console
print("hello world")

# create rock, paper, scissors game

# get game intro, get input from user to pick rock, paper, or scissors / lower input from user also check string input

# inform if the user won, lost, or tied, display score and ask if player can play again, if user types screen play again

print("Welcome to Rock, Paper, Scissors!")
import random

print("Type 'rock', 'paper', or 'scissors' to play!")
def play_game():
    user_choice = input("Enter your choice: ").lower()
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        return

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

    # ask if player can play again with the text input 'again' or 'screen'
    play_again = input("Do you want to play again? (yes type again - no type screen): ").lower()
    if play_again == "yes" or play_again == "again":
        play_game()
    elif play_again == "no" or play_again == "screen":
        print("Thanks for playing!")
    else:
        print("Invalid input. Please type 'yes or again' or 'no or screen'.")
        

play_game()

