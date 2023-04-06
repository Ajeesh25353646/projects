
# the program randomly selects a secret word 
# from a list of secret words. 
# The user has to guess the letters
# of the word one by one. 
# The user has a limited number of guesses
# and for every incorrect guess, 
# a part of a stick figure is drawn.
# If the stick figure is completed
# before the user guesses the word correctly, they lose 2.
import random


list_of_words = ["lion", "tiger", "elephant", "bear", "panda"]
    
# computer selects a random secret word from list
secret_word = random.choice(list_of_words)
print("Hint: secret word is an animal\n") 

correct_guess = ['_'] * len(secret_word)
star_drawn = ""
incorrect_guess = 0  

while True:
    # player guess
    guess = input("guess the letter in word \nor write exit to exit the game: ")
    guess = guess.lower()

    if guess == "exit":
        exit()
    
    if guess in correct_guess or guess in star_drawn:
        print("\nYou already guessed that letter!")
        continue
    
    if guess in secret_word:
        print("correct letter guess")
        for index, char in enumerate(list(secret_word)):
            if char == guess:
                correct_guess[index] = char
    else:
        print("wrong guess")
        star_drawn += "*"
        incorrect_guess += 1
        
    print("".join(correct_guess))
    print(f"stars will be drawn here, 3 stars means 3 incorrect answers and then game is over:\n{star_drawn}\n")

    # 3 incorrect answers mean game over, here u can change no of chances u get
    if incorrect_guess == 3:
        print("GAME OVER")
        print(f"CORRECT ANSWER: {secret_word}")
        exit()
    elif '_' not in correct_guess:
        print("you guessed the word right \nyou won the game")
        break
    









