############# snake water gun ####################
import random 

print("write exit to exit the game")

while True:
    player_move = input("choose snake,water or gun: ")
    if player_move == "exit":
        break
    else:
        all_possible_move = ["snake","water","gun"]
        computer_move = random.choice(all_possible_move)
        print(f"computer chose {computer_move}")
        outcomes = [["d","w","l"],["l","d","w"],["w","l","d"]]


        # custom error if someone put in some random wrong input 
        # which does not makes sense 
        try:    
            x = all_possible_move.index(player_move)
        except:
            print("invalid input\nput snake,water or gun as input")
            continue

        y = all_possible_move.index(computer_move)
        res = outcomes[y][x]
        if res == "w":
            print("you won, congrats")
        elif res == "l":
            print("you lose, better luck next time")
        elif res == "d":
            print("its a draw")



