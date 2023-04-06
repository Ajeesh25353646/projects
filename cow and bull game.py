############ cow and bull game ##########
### project idea taken from pythonorg.in
# made by - Ajeesh



# Create a program that will play 
# the “cows and bulls” game with the user. 
# The game works like this:

# Randomly generate a 4-digit number. 
# Ask the user to guess a 4-digit number. 
# For every digit that the user guessed correctly
# in the correct place, they have a “cow”. 
# For every digit the user guessed correctly 
# in the wrong place is a “bull.”
# Every time the user makes a guess,
# tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user 
# makes throughout teh game and tell the user at the end.

import random

def main():
    generated = random.randint(1000,9999)
    no_of_guesses = 0
    while True:
        try:
            guess = input("Enter your 4 digit no guess: ")
            if guess == "exit":
                break
            guess = int(guess)
            if not 1000 <= guess <= 9999:
                raise ValueError("Invalid input. Please enter a 4-digit number or 'exit'.")
            no_of_guesses += 1
            if guess == generated:
                print("Game is over, guess is correct.")
                break
            else:
                cow_no = 0
                bull_no = 0
                generate_list = list(str(generated))
                guess_list = list(str(guess))
                for i in range(len(generate_list)):
                    if generate_list[i] == guess_list[i]:
                        cow_no += 1
                    elif guess_list[i] in generate_list:
                        bull_no += 1
                print(f"You have {cow_no} cows and {bull_no} bulls.")
        except ValueError as e:
            print(e)

    print(f"The correct answer was {generated} and you made {no_of_guesses} guesses.")

if __name__ == "__main__":
    main()
