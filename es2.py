""" EXERCISE 2
Make a rock-paper-scissors game to play against the computer. The game should ask the user for input, generate
a random choice for the computer, compare the two and print the result. The player should be able to play again until
they choose to stop by writing "quit"."""
#quack quack quack

# Import the random module
from random import choice

# Define the possible choices
choices = ["rock", "paper", "scissors"]


# Define the function that will play the game
def play(play_again: bool = True) -> bool:
    # Ask the user for input
    user_choice = input("Choose rock, paper or scissors: ")

    # Generate a random choice for the computer
    computer_choice = choice(choices)

    # Check if the user wants to quit
    if user_choice == "quit":
        play_again = False
        return play_again

    # Create a string that tells the user what they chose and what the computer chose.
    # There are many ways to create a string. In this case, we use f-strings.
    # f-strings are a way to create a string that contains variables.
    # The syntax is f"string {variable} string" where the variable is the name of the variable between curly brackets.
    output_str = f"You chose {user_choice} and the computer chose {computer_choice}. "

    # Compare the two and print the result
    if user_choice == computer_choice:
        print(output_str + "It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print(output_str + "You lose!")
        else:
            print(output_str + "You win!")
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print(output_str + "You lose!")
        else:
            print(output_str + "You win!")
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print(output_str + "You lose!")
        else:
            print(output_str + "You win!")
    else:
        print("Invalid input!")
    return play_again


# Define the function that will run the game
if __name__ == "__main__":
    play_again = True
    while play_again:
        play_again = play(play_again)
    print("Thanks for playing!")
