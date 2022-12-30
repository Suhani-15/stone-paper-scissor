import random

while True:
    user_input = input("enter your choice (rock,paper,scissor)")
    possible_choice = ["rock","paper","scissor"]
    computer_input = random.choice(possible_choice)
    print(f"you chose{user_input}, computer chose {computer_input}")
    if user_input == computer_input:
        print(f"Its a draw as both selected {user_input}")
    elif user_input == "rock":
            if computer_input == "scissor":
                print("User wins, rock will break the scissor")
            else:
                print("User lose, paper will cover rock")
    elif user_input == "paper":
            if computer_input == "rock":
                print("User wins, paper will cover rock")
            else:
                print("User lose, scissor will cut the paper")
    elif user_input == "scissor":
            if computer_input == "paper":
                 print("User wins, scissor will cut the paper")
            else:
                print("User lose, rock will break the scissor")
    
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break

print("Game Over")





